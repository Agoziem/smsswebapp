from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import School
from ..schemas import (
    SchoolCreateSchema,
    SchoolUpdateSchema,
    SchoolResponseSchema,
    SuccessResponseSchema
)

@api_controller("/schools", tags=["Schools"])
class SchoolController:

    @route.get("/", response=List[SchoolResponseSchema])
    def list_schools(self):
        """Get all schools"""
        return School.objects.all()

    @route.get("/{school_id}", response=SchoolResponseSchema)
    def get_school(self, school_id: int):
        """Get a specific school by ID"""
        return get_object_or_404(School, id=school_id)

    @route.post("/", response=SchoolResponseSchema)
    def create_school(self, payload: SchoolCreateSchema):
        """Create a new school"""
        return School.objects.create(**payload.model_dump())

    @route.put("/{school_id}", response=SchoolResponseSchema)
    def update_school(self, school_id: int, payload: SchoolUpdateSchema):
        """Update an existing school"""
        school = get_object_or_404(School, id=school_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(school, key, value)
        
        school.save()
        return school

    @route.delete("/{school_id}", response={200: SuccessResponseSchema, 404: "School not found"})
    def delete_school(self, school_id: int):
        """Delete a school"""
        school = get_object_or_404(School, id=school_id)
        school.delete()
        return {"message": "School deleted successfully"}
