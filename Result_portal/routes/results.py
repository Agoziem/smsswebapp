from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route
from typing import List, Optional
from ..models import Student_Result_Data, Result, AnnualStudent, AnnualResult
from ..schemas import (
    StudentResultDataCreateSchema, StudentResultDataUpdateSchema, StudentResultDataResponseSchema,
    ResultCreateSchema, ResultUpdateSchema, ResultResponseSchema,
    AnnualStudentCreateSchema, AnnualStudentUpdateSchema, AnnualStudentResponseSchema,
    AnnualResultCreateSchema, AnnualResultUpdateSchema, AnnualResultResponseSchema,
    SuccessResponseSchema
)


@api_controller('/student-result-data', tags=['Student Result Data'])
class StudentResultDataController:
    """Controller for managing student result data"""
    
    @route.get('/', response=List[StudentResultDataResponseSchema], summary="Get all student result data")
    def list_student_result_data(self, published: Optional[bool] = None):
        """Get all student result data, optionally filter by published status"""
        queryset = Student_Result_Data.objects.all()
        if published is not None:
            queryset = queryset.filter(published=published)
        return queryset
    
    @route.get('/{int:id}', response=StudentResultDataResponseSchema, summary="Get student result data by ID")
    def get_student_result_data(self, id: int):
        """Get a specific student result data by ID"""
        return get_object_or_404(Student_Result_Data, id=id)
    
    @route.post('/', response=StudentResultDataResponseSchema, summary="Create new student result data")
    def create_student_result_data(self, payload: StudentResultDataCreateSchema):
        """Create a new student result data"""
        return Student_Result_Data.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=StudentResultDataResponseSchema, summary="Update student result data")
    def update_student_result_data(self, id: int, payload: StudentResultDataUpdateSchema):
        """Update an existing student result data"""
        student_result = get_object_or_404(Student_Result_Data, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(student_result, attr, value)
        student_result.save()
        return student_result
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete student result data")
    def delete_student_result_data(self, id: int):
        """Delete a student result data"""
        student_result = get_object_or_404(Student_Result_Data, id=id)
        student_result.delete()
        return {"message": "Student result data deleted successfully"}


@api_controller('/results', tags=['Results'])
class ResultController:
    """Controller for managing individual subject results"""
    
    @route.get('/', response=List[ResultResponseSchema], summary="Get all results")
    def list_results(self, published: Optional[bool] = None, student_id: Optional[int] = None):
        """Get all results, optionally filter by published status or student"""
        queryset = Result.objects.all()
        if published is not None:
            queryset = queryset.filter(published=published)
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        return queryset
    
    @route.get('/{int:id}', response=ResultResponseSchema, summary="Get result by ID")
    def get_result(self, id: int):
        """Get a specific result by ID"""
        return get_object_or_404(Result, id=id)
    
    @route.post('/', response=ResultResponseSchema, summary="Create new result")
    def create_result(self, payload: ResultCreateSchema):
        """Create a new result"""
        return Result.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=ResultResponseSchema, summary="Update result")
    def update_result(self, id: int, payload: ResultUpdateSchema):
        """Update an existing result"""
        result = get_object_or_404(Result, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(result, attr, value)
        result.save()
        return result
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete result")
    def delete_result(self, id: int):
        """Delete a result"""
        result = get_object_or_404(Result, id=id)
        result.delete()
        return {"message": "Result deleted successfully"}


@api_controller('/annual-students', tags=['Annual Students'])
class AnnualStudentController:
    """Controller for managing annual student data"""
    
    @route.get('/', response=List[AnnualStudentResponseSchema], summary="Get all annual students")
    def list_annual_students(self, published: Optional[bool] = None):
        """Get all annual students, optionally filter by published status"""
        queryset = AnnualStudent.objects.all()
        if published is not None:
            queryset = queryset.filter(published=published)
        return queryset
    
    @route.get('/{int:id}', response=AnnualStudentResponseSchema, summary="Get annual student by ID")
    def get_annual_student(self, id: int):
        """Get a specific annual student by ID"""
        return get_object_or_404(AnnualStudent, id=id)
    
    @route.post('/', response=AnnualStudentResponseSchema, summary="Create new annual student")
    def create_annual_student(self, payload: AnnualStudentCreateSchema):
        """Create a new annual student"""
        return AnnualStudent.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=AnnualStudentResponseSchema, summary="Update annual student")
    def update_annual_student(self, id: int, payload: AnnualStudentUpdateSchema):
        """Update an existing annual student"""
        annual_student = get_object_or_404(AnnualStudent, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(annual_student, attr, value)
        annual_student.save()
        return annual_student
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete annual student")
    def delete_annual_student(self, id: int):
        """Delete an annual student"""
        annual_student = get_object_or_404(AnnualStudent, id=id)
        annual_student.delete()
        return {"message": "Annual student deleted successfully"}


@api_controller('/annual-results', tags=['Annual Results'])
class AnnualResultController:
    """Controller for managing annual results"""
    
    @route.get('/', response=List[AnnualResultResponseSchema], summary="Get all annual results")
    def list_annual_results(self, published: Optional[bool] = None, student_id: Optional[int] = None):
        """Get all annual results, optionally filter by published status or student"""
        queryset = AnnualResult.objects.all()
        if published is not None:
            queryset = queryset.filter(published=published)
        if student_id is not None:
            queryset = queryset.filter(student_name_id=student_id)
        return queryset
    
    @route.get('/{int:id}', response=AnnualResultResponseSchema, summary="Get annual result by ID")
    def get_annual_result(self, id: int):
        """Get a specific annual result by ID"""
        return get_object_or_404(AnnualResult, id=id)
    
    @route.post('/', response=AnnualResultResponseSchema, summary="Create new annual result")
    def create_annual_result(self, payload: AnnualResultCreateSchema):
        """Create a new annual result"""
        return AnnualResult.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=AnnualResultResponseSchema, summary="Update annual result")
    def update_annual_result(self, id: int, payload: AnnualResultUpdateSchema):
        """Update an existing annual result"""
        annual_result = get_object_or_404(AnnualResult, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(annual_result, attr, value)
        annual_result.save()
        return annual_result
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete annual result")
    def delete_annual_result(self, id: int):
        """Delete an annual result"""
        annual_result = get_object_or_404(AnnualResult, id=id)
        annual_result.delete()
        return {"message": "Annual result deleted successfully"}
