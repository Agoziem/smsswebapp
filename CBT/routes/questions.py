from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Question, Answer
from ..schemas import (
    QuestionCreateSchema,
    QuestionUpdateSchema,
    QuestionResponseSchema,
    QuestionDeleteSchema,
    AnswerResponseSchema
)

router = Router(tags=["Questions"])


@router.get("/", response=List[QuestionResponseSchema])
def list_questions(request):
    """Get all questions"""
    questions = Question.objects.prefetch_related('answers').all()
    return [
        QuestionResponseSchema(
            id=question.pk,
            question_id=question.questionId,
            question_text=question.questiontext if question.questiontext else "",
            question_mark=question.questionMark,
            required=question.required,
            answers=[
                AnswerResponseSchema(
                    id=answer.pk,
                    answer_id=answer.answerId,
                    answer_text=answer.answertext,
                    is_correct=answer.isCorrect
                ) for answer in question.answers.all()
            ]
        ) for question in questions
    ]


@router.get("/{question_id}", response=QuestionResponseSchema)
def get_question(request, question_id: int):
    """Get a specific question by ID"""
    question = get_object_or_404(Question.objects.prefetch_related('answers'), id=question_id)
    return QuestionResponseSchema(
        id=question.pk,
        question_id=question.questionId,
        question_text=question.questiontext if question.questiontext else "",
        question_mark=question.questionMark,
        required=question.required,
        answers=[
            AnswerResponseSchema(
                id=answer.pk,
                answer_id=answer.answerId,
                answer_text=answer.answertext,
                is_correct=answer.isCorrect
            ) for answer in question.answers.all()
        ]
    )


@router.post("/", response=QuestionResponseSchema)
def create_question(request, payload: QuestionCreateSchema):
    """Create a new question"""
    question_data = payload.dict(exclude={'answer_ids'})
    question = Question.objects.create(
        questionId=question_data['question_id'],
        questiontext=question_data['question_text'],
        questionMark=question_data['question_mark'],
        required=question_data['required']
    )
    
    # Add answers if provided
    if payload.answer_ids:
        answers = Answer.objects.filter(id__in=payload.answer_ids)
        question.answers.set(answers)
    
    return QuestionResponseSchema(
        id=question.pk,
        question_id=question.questionId,
        question_text=question.questiontext if question.questiontext else "",
        question_mark=question.questionMark,
        required=question.required,
        answers=[
            AnswerResponseSchema(
                id=answer.pk,
                answer_id=answer.answerId,
                answer_text=answer.answertext,
                is_correct=answer.isCorrect
            ) for answer in question.answers.all()
        ]
    )


@router.put("/{question_id}", response=QuestionResponseSchema)
def update_question(request, question_id: int, payload: QuestionUpdateSchema):
    """Update an existing question"""
    question = get_object_or_404(Question, id=question_id)
    
    update_data = payload.dict(exclude_unset=True, exclude={'answer_ids'})
    field_mapping = {
        'question_id': 'questionId',
        'question_text': 'questiontext',
        'question_mark': 'questionMark',
        'required': 'required'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(question, model_field, value)
    
    question.save()
    
    # Update answers if provided
    if payload.answer_ids is not None:
        answers = Answer.objects.filter(id__in=payload.answer_ids)
        question.answers.set(answers)
    
    return QuestionResponseSchema(
        id=question.pk,
        question_id=question.questionId,
        question_text=question.questiontext if question.questiontext else "",
        question_mark=question.questionMark,
        required=question.required,
        answers=[
            AnswerResponseSchema(
                id=answer.pk,
                answer_id=answer.answerId,
                answer_text=answer.answertext,
                is_correct=answer.isCorrect
            ) for answer in question.answers.all()
        ]
    )


@router.delete("/{question_id}", response=QuestionDeleteSchema)
def delete_question(request, question_id: int):
    """Delete a question"""
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return QuestionDeleteSchema(deleted_id=question_id)
