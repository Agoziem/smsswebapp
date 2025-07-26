from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route
from typing import List, Optional
from ..models import Students_Pin_and_ID, StudentClassEnrollment
from ..schemas import (
    StudentsPinAndIDCreateSchema, StudentsPinAndIDUpdateSchema, StudentsPinAndIDResponseSchema,
    StudentClassEnrollmentCreateSchema, StudentClassEnrollmentUpdateSchema, StudentClassEnrollmentResponseSchema,
    SuccessResponseSchema
)


@api_controller('/students', tags=['Students'])
class StudentController:
    """Controller for managing students"""
    
    @route.get('/', response=List[StudentsPinAndIDResponseSchema], summary="Get all students")
    def list_students(self, sex: Optional[str] = None):
        """Get all students, optionally filter by sex"""
        queryset = Students_Pin_and_ID.objects.all()
        if sex is not None:
            queryset = queryset.filter(Sex=sex)
        return queryset
    
    @route.get('/{int:id}', response=StudentsPinAndIDResponseSchema, summary="Get student by ID")
    def get_student(self, id: int):
        """Get a specific student by ID"""
        return get_object_or_404(Students_Pin_and_ID, id=id)
    
    @route.post('/', response=StudentsPinAndIDResponseSchema, summary="Create new student")
    def create_student(self, payload: StudentsPinAndIDCreateSchema):
        """Create a new student"""
        return Students_Pin_and_ID.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=StudentsPinAndIDResponseSchema, summary="Update student")
    def update_student(self, id: int, payload: StudentsPinAndIDUpdateSchema):
        """Update an existing student"""
        student = get_object_or_404(Students_Pin_and_ID, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(student, attr, value)
        student.save()
        return student
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete student")
    def delete_student(self, id: int):
        """Delete a student"""
        student = get_object_or_404(Students_Pin_and_ID, id=id)
        student.delete()
        return {"message": "Student deleted successfully"}


@api_controller('/student-enrollments', tags=['Student Enrollments'])
class StudentEnrollmentController:
    """Controller for managing student class enrollments"""
    
    @route.get('/', response=List[StudentClassEnrollmentResponseSchema], summary="Get all student enrollments")
    def list_enrollments(self, student_id: Optional[int] = None, class_id: Optional[int] = None):
        """Get all student enrollments, optionally filter by student or class"""
        queryset = StudentClassEnrollment.objects.all()
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        if class_id is not None:
            queryset = queryset.filter(student_class_id=class_id)
        return queryset
    
    @route.get('/{int:id}', response=StudentClassEnrollmentResponseSchema, summary="Get enrollment by ID")
    def get_enrollment(self, id: int):
        """Get a specific enrollment by ID"""
        return get_object_or_404(StudentClassEnrollment, id=id)
    
    @route.post('/', response=StudentClassEnrollmentResponseSchema, summary="Create new enrollment")
    def create_enrollment(self, payload: StudentClassEnrollmentCreateSchema):
        """Create a new student enrollment"""
        return StudentClassEnrollment.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=StudentClassEnrollmentResponseSchema, summary="Update enrollment")
    def update_enrollment(self, id: int, payload: StudentClassEnrollmentUpdateSchema):
        """Update an existing enrollment"""
        enrollment = get_object_or_404(StudentClassEnrollment, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(enrollment, attr, value)
        enrollment.save()
        return enrollment
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete enrollment")
    def delete_enrollment(self, id: int):
        """Delete an enrollment"""
        enrollment = get_object_or_404(StudentClassEnrollment, id=id)
        enrollment.delete()
        return {"message": "Student enrollment deleted successfully"}

def create_student_enrollment(request, payload: StudentClassEnrollmentCreateSchema):
    """Create a new student enrollment"""
    from ..models import Class, AcademicSession
    
    student = get_object_or_404(Students_Pin_and_ID, id=payload.student_id)
    student_class = get_object_or_404(Class, id=payload.student_class_id)
    academic_session = get_object_or_404(AcademicSession, id=payload.academic_session_id)
    

