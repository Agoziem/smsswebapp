from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import Answer
from ..schemas import (
    AnswerCreateSchema,
    AnswerUpdateSchema,
    AnswerResponseSchema,
    SuccessResponseSchema
)

@api_controller("/answers", tags=["Answers"])
class AnswerController:

    @route.get("/", response=List[AnswerResponseSchema])
    def list_answers(self):
        """Get all answers"""
        return Answer.objects.all()

    @route.get("/{answer_id}", response=AnswerResponseSchema)
    def get_answer(self, answer_id: int):
        """Get a specific answer by ID"""
        return get_object_or_404(Answer, id=answer_id)

    @route.post("/", response=AnswerResponseSchema)
    def create_answer(self, payload: AnswerCreateSchema):
        """Create a new answer"""
        return Answer.objects.create(**payload.model_dump())

    @route.put("/{answer_id}", response=AnswerResponseSchema)
    def update_answer(self, answer_id: int, payload: AnswerUpdateSchema):
        """Update an existing answer"""
        answer = get_object_or_404(Answer, id=answer_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(answer, key, value)
        
        answer.save()
        return answer

    @route.delete("/{answer_id}", response={200: SuccessResponseSchema, 404: "Answer not found"})
    def delete_answer(self, answer_id: int):
        """Delete an answer"""
        answer = get_object_or_404(Answer, id=answer_id)
        answer.delete()
        return {"message": "Answer deleted successfully"}
