from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import Question, Answer
from ..schemas import (
    QuestionCreateSchema,
    QuestionUpdateSchema,
    QuestionResponseSchema,
    SuccessResponseSchema
)

@api_controller("/questions", tags=["Questions"])
class QuestionController:

    @route.get("/", response=List[QuestionResponseSchema])
    def list_questions(self):
        """Get all questions"""
        return Question.objects.prefetch_related('answers').all()

    @route.get("/{question_id}", response=QuestionResponseSchema)
    def get_question(self, question_id: int):
        """Get a specific question by ID"""
        return get_object_or_404(Question.objects.prefetch_related('answers'), id=question_id)

    @route.post("/", response=QuestionResponseSchema)
    def create_question(self, payload: QuestionCreateSchema):
        """Create a new question"""
        question_data = payload.model_dump(exclude={'answer_ids'})
        question = Question.objects.create(**question_data)
        
        # Add answers if provided
        if payload.answer_ids:
            answers = Answer.objects.filter(id__in=payload.answer_ids)
            question.answers.set(answers)
        
        return question

    @route.put("/{question_id}", response=QuestionResponseSchema)
    def update_question(self, question_id: int, payload: QuestionUpdateSchema):
        """Update an existing question"""
        question = get_object_or_404(Question, id=question_id)
        
        update_data = payload.model_dump(exclude_unset=True, exclude={'answer_ids'})
        for key, value in update_data.items():
            setattr(question, key, value)
        
        question.save()
        
        # Update answers if provided
        if payload.answer_ids is not None:
            answers = Answer.objects.filter(id__in=payload.answer_ids)
            question.answers.set(answers)
        
        return question

    @route.delete("/{question_id}", response={200: SuccessResponseSchema, 404: "Question not found"})
    def delete_question(self, question_id: int):
        """Delete a question"""
        question = get_object_or_404(Question, id=question_id)
        question.delete()
        return {"message": "Question deleted successfully"}
