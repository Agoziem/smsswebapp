from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Test
from ..schemas import (
    TestCreateSchema,
    TestUpdateSchema,
    TestResponseSchema,
    TestDeleteSchema
)

router = Router(tags=["Tests"])


@router.get("/", response=List[TestResponseSchema])
def list_tests(request):
    """Get all tests"""
    tests = Test.objects.all()
    return [TestResponseSchema.model_validate(test) for test in tests]


@router.get("/{test_id}", response=TestResponseSchema)
def get_test(request, test_id: int):
    """Get a specific test by ID"""
    test = get_object_or_404(Test, id=test_id)
    return TestResponseSchema.model_validate(test)


@router.post("/", response=TestResponseSchema)
def create_test(request, payload: TestCreateSchema):
    """Create a new test"""
    test = Test.objects.create(**payload.dict())
    return TestResponseSchema.model_validate(test)


@router.put("/{test_id}", response=TestResponseSchema)
def update_test(request, test_id: int, payload: TestUpdateSchema):
    """Update an existing test"""
    test = get_object_or_404(Test, id=test_id)
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(test, key, value)
    
    test.save()
    return TestResponseSchema.model_validate(test)


@router.delete("/{test_id}", response=TestDeleteSchema)
def delete_test(request, test_id: int):
    """Delete a test"""
    test = get_object_or_404(Test, id=test_id)
    test.delete()
    return TestDeleteSchema(deleted_id=test_id)
