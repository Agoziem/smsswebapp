from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Answer
from ..schemas import (
    AnswerCreateSchema,
    AnswerUpdateSchema,
    AnswerResponseSchema,
    AnswerDeleteSchema
)

router = Router(tags=["Answers"])


@router.get("/", response=List[AnswerResponseSchema])
def list_answers(request):
    """Get all answers"""
    answers = Answer.objects.all()
    return [
        AnswerResponseSchema(
            id=answer.pk,
            answer_id=answer.answerId,
            answer_text=answer.answertext,
            is_correct=answer.isCorrect
        ) for answer in answers
    ]


@router.get("/{answer_id}", response=AnswerResponseSchema)
def get_answer(request, answer_id: int):
    """Get a specific answer by ID"""
    answer = get_object_or_404(Answer, id=answer_id)
    return AnswerResponseSchema(
        id=answer.pk,
        answer_id=answer.answerId,
        answer_text=answer.answertext,
        is_correct=answer.isCorrect
    )


@router.post("/", response=AnswerResponseSchema)
def create_answer(request, payload: AnswerCreateSchema):
    """Create a new answer"""
    answer = Answer.objects.create(
        answerId=payload.answer_id,
        answertext=payload.answer_text,
        isCorrect=payload.is_correct
    )
    return AnswerResponseSchema(
        id=answer.pk,
        answer_id=answer.answerId,
        answer_text=answer.answertext,
        is_correct=answer.isCorrect
    )


@router.put("/{answer_id}", response=AnswerResponseSchema)
def update_answer(request, answer_id: int, payload: AnswerUpdateSchema):
    """Update an existing answer"""
    answer = get_object_or_404(Answer, id=answer_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'answer_id': 'answerId',
        'answer_text': 'answertext',
        'is_correct': 'isCorrect'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(answer, model_field, value)
    
    answer.save()
    return AnswerResponseSchema(
        id=answer.pk,
        answer_id=answer.answerId,
        answer_text=answer.answertext,
        is_correct=answer.isCorrect
    )


@router.delete("/{answer_id}", response=AnswerDeleteSchema)
def delete_answer(request, answer_id: int):
    """Delete an answer"""
    answer = get_object_or_404(Answer, id=answer_id)
    answer.delete()
    return AnswerDeleteSchema(deleted_id=answer_id)
