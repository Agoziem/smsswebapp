from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import Test
from ..schemas import (
    TestCreateSchema,
    TestUpdateSchema,
    TestResponseSchema,
    SuccessResponseSchema
)

@api_controller("/tests", tags=["Tests"])
class TestController:

    @route.get("/", response=List[TestResponseSchema])
    def list_tests(self):
        """Get all tests"""
        return Test.objects.all()

    @route.get("/{test_id}", response=TestResponseSchema)
    def get_test(self, test_id: int):
        """Get a specific test by ID"""
        return get_object_or_404(Test, id=test_id)

    @route.post("/", response=TestResponseSchema)
    def create_test(self, payload: TestCreateSchema):
        """Create a new test"""
        return Test.objects.create(**payload.model_dump())

    @route.put("/{test_id}", response=TestResponseSchema)
    def update_test(self, test_id: int, payload: TestUpdateSchema):
        """Update an existing test"""
        test = get_object_or_404(Test, id=test_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(test, key, value)
        
        test.save()
        return test

    @route.delete("/{test_id}", response={200: SuccessResponseSchema, 404: "Test not found"})
    def delete_test(self, test_id: int):
        """Delete a test"""
        test = get_object_or_404(Test, id=test_id)
        test.delete()
        return {"message": "Test deleted successfully"}
