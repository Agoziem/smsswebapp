from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route
from typing import List, Optional
from ..models import Teacher, Attendance
from ..schemas import (
    TeacherCreateSchema, TeacherUpdateSchema, TeacherResponseSchema,
    AttendanceCreateSchema, AttendanceUpdateSchema, AttendanceResponseSchema,
    SuccessResponseSchema
)


@api_controller('/teachers', tags=['Teachers'])
class TeacherController:
    """Controller for managing teachers"""
    
    @route.get('/', response=List[TeacherResponseSchema], summary="Get all teachers")
    def list_teachers(self, subject: Optional[str] = None):
        """Get all teachers, optionally filter by subject"""
        queryset = Teacher.objects.all()
        if subject is not None:
            queryset = queryset.filter(subject__icontains=subject)
        return queryset
    
    @route.get('/{int:id}', response=TeacherResponseSchema, summary="Get teacher by ID")
    def get_teacher(self, id: int):
        """Get a specific teacher by ID"""
        return get_object_or_404(Teacher, id=id)
    
    @route.post('/', response=TeacherResponseSchema, summary="Create new teacher")
    def create_teacher(self, payload: TeacherCreateSchema):
        """Create a new teacher"""
        return Teacher.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=TeacherResponseSchema, summary="Update teacher")
    def update_teacher(self, id: int, payload: TeacherUpdateSchema):
        """Update an existing teacher"""
        teacher = get_object_or_404(Teacher, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(teacher, attr, value)
        teacher.save()
        return teacher
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete teacher")
    def delete_teacher(self, id: int):
        """Delete a teacher"""
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return {"message": "Teacher deleted successfully"}
