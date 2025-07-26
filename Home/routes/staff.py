from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import Management, TopTeacher
from ..schemas import (
    ManagementCreateSchema,
    ManagementUpdateSchema,
    ManagementResponseSchema,
    TopTeacherCreateSchema,
    TopTeacherUpdateSchema,
    TopTeacherResponseSchema,
    SuccessResponseSchema
)

@api_controller("/management", tags=["Management"])
class ManagementController:

    @route.get("/", response=List[ManagementResponseSchema])
    def list_management(self):
        """Get all management profiles"""
        return Management.objects.all()

    @route.get("/{management_id}", response=ManagementResponseSchema)
    def get_management(self, management_id: int):
        """Get a specific management profile by ID"""
        return get_object_or_404(Management, id=management_id)

    @route.post("/", response=ManagementResponseSchema)
    def create_management(self, payload: ManagementCreateSchema):
        """Create a new management profile"""
        return Management.objects.create(**payload.model_dump())

    @route.put("/{management_id}", response=ManagementResponseSchema)
    def update_management(self, management_id: int, payload: ManagementUpdateSchema):
        """Update an existing management profile"""
        management = get_object_or_404(Management, id=management_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(management, key, value)
        
        management.save()
        return management

    @route.delete("/{management_id}", response={200: SuccessResponseSchema, 404: "Management not found"})
    def delete_management(self, management_id: int):
        """Delete a management profile"""
        management = get_object_or_404(Management, id=management_id)
        management.delete()
        return {"message": "Management profile deleted successfully"}


@api_controller("/top-teachers", tags=["Top Teachers"])
class TopTeacherController:

    @route.get("/", response=List[TopTeacherResponseSchema])
    def list_top_teachers(self):
        """Get all top teachers"""
        return TopTeacher.objects.all()

    @route.get("/{teacher_id}", response=TopTeacherResponseSchema)
    def get_top_teacher(self, teacher_id: int):
        """Get a specific top teacher by ID"""
        return get_object_or_404(TopTeacher, id=teacher_id)

    @route.post("/", response=TopTeacherResponseSchema)
    def create_top_teacher(self, payload: TopTeacherCreateSchema):
        """Create a new top teacher"""
        return TopTeacher.objects.create(**payload.model_dump())

    @route.put("/{teacher_id}", response=TopTeacherResponseSchema)
    def update_top_teacher(self, teacher_id: int, payload: TopTeacherUpdateSchema):
        """Update an existing top teacher"""
        teacher = get_object_or_404(TopTeacher, id=teacher_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(teacher, key, value)
        
        teacher.save()
        return teacher

    @route.delete("/{teacher_id}", response={200: SuccessResponseSchema, 404: "Top Teacher not found"})
    def delete_top_teacher(self, teacher_id: int):
        """Delete a top teacher"""
        teacher = get_object_or_404(TopTeacher, id=teacher_id)
        teacher.delete()
        return {"message": "Top teacher deleted successfully"}
