from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Students_Pin_and_ID, StudentClassEnrollment
from ..schemas import (
    StudentsCreateSchema,
    StudentsUpdateSchema,
    StudentsResponseSchema,
    StudentsDeleteSchema,
    StudentClassEnrollmentCreateSchema,
    StudentClassEnrollmentUpdateSchema,
    StudentClassEnrollmentResponseSchema,
    StudentClassEnrollmentDeleteSchema
)

students_router = Router(tags=["Students"])
enrollment_router = Router(tags=["Student Enrollments"])


# Students routes
@students_router.get("/", response=List[StudentsResponseSchema])
def list_students(request):
    """Get all students"""
    students = Students_Pin_and_ID.objects.all()
    return [
        StudentsResponseSchema(
            id=student.pk,
            sn=student.SN,
            student_name=student.student_name if student.student_name else "Not Available",
            student_id=student.student_id,
            sex=student.Sex,
            student_pin=student.student_pin,
            student_photo=student.student_Photo.url if student.student_Photo else None
        ) for student in students
    ]


@students_router.get("/{student_id}", response=StudentsResponseSchema)
def get_student(request, student_id: int):
    """Get a specific student by ID"""
    student = get_object_or_404(Students_Pin_and_ID, id=student_id)
    return StudentsResponseSchema(
        id=student.pk,
        sn=student.SN,
        student_name=student.student_name if student.student_name else "Not Available",
        student_id=student.student_id,
        sex=student.Sex,
        student_pin=student.student_pin,
        student_photo=student.student_Photo.url if student.student_Photo else None
    )


@students_router.post("/", response=StudentsResponseSchema)
def create_student(request, payload: StudentsCreateSchema):
    """Create a new student"""
    student = Students_Pin_and_ID.objects.create(
        SN=payload.sn,
        student_Photo=payload.student_photo,
        student_name=payload.student_name,
        Sex=payload.sex,
        student_password=payload.student_password
    )
    
    return StudentsResponseSchema(
        id=student.pk,
        sn=student.SN,
        student_name=student.student_name if student.student_name else "Not Available",
        student_id=student.student_id,
        sex=student.Sex,
        student_pin=student.student_pin,
        student_photo=student.student_Photo.url if student.student_Photo else None
    )


@students_router.put("/{student_id}", response=StudentsResponseSchema)
def update_student(request, student_id: int, payload: StudentsUpdateSchema):
    """Update an existing student"""
    student = get_object_or_404(Students_Pin_and_ID, id=student_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'sn': 'SN',
        'student_photo': 'student_Photo',
        'student_name': 'student_name',
        'sex': 'Sex',
        'student_password': 'student_password'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(student, model_field, value)
    
    student.save()
    
    return StudentsResponseSchema(
        id=student.pk,
        sn=student.SN,
        student_name=student.student_name if student.student_name else "Not Available",
        student_id=student.student_id,
        sex=student.Sex,
        student_pin=student.student_pin,
        student_photo=student.student_Photo.url if student.student_Photo else None
    )


@students_router.delete("/{student_id}", response=StudentsDeleteSchema)
def delete_student(request, student_id: int):
    """Delete a student"""
    student = get_object_or_404(Students_Pin_and_ID, id=student_id)
    student.delete()
    return StudentsDeleteSchema(deleted_id=student_id)


# Student Enrollment routes
@enrollment_router.get("/", response=List[StudentClassEnrollmentResponseSchema])
def list_student_enrollments(request):
    """Get all student enrollments"""
    enrollments = StudentClassEnrollment.objects.select_related('student', 'student_class', 'academic_session').all()
    return [
        StudentClassEnrollmentResponseSchema(
            id=enrollment.pk,
            student_name=enrollment.student.student_name if enrollment.student else None,
            class_name=enrollment.student_class.Class if enrollment.student_class else None,
            academic_session=enrollment.academic_session.session if enrollment.academic_session else None
        ) for enrollment in enrollments
    ]


@enrollment_router.get("/{enrollment_id}", response=StudentClassEnrollmentResponseSchema)
def get_student_enrollment(request, enrollment_id: int):
    """Get a specific student enrollment by ID"""
    enrollment = get_object_or_404(
        StudentClassEnrollment.objects.select_related('student', 'student_class', 'academic_session'),
        id=enrollment_id
    )
    return StudentClassEnrollmentResponseSchema(
        id=enrollment.pk,
        student_name=enrollment.student.student_name if enrollment.student else None,
        class_name=enrollment.student_class.Class if enrollment.student_class else None,
        academic_session=enrollment.academic_session.session if enrollment.academic_session else None
    )


@enrollment_router.post("/", response=StudentClassEnrollmentResponseSchema)
def create_student_enrollment(request, payload: StudentClassEnrollmentCreateSchema):
    """Create a new student enrollment"""
    from ..models import Class, AcademicSession
    
    student = get_object_or_404(Students_Pin_and_ID, id=payload.student_id)
    student_class = get_object_or_404(Class, id=payload.student_class_id)
    academic_session = get_object_or_404(AcademicSession, id=payload.academic_session_id)
    
    enrollment = StudentClassEnrollment.objects.create(
        student=student,
        student_class=student_class,
        academic_session=academic_session
    )
    
    return StudentClassEnrollmentResponseSchema(
        id=enrollment.pk,
        student_name=enrollment.student.student_name,
        class_name=enrollment.student_class.Class,
        academic_session=enrollment.academic_session.session
    )


@enrollment_router.put("/{enrollment_id}", response=StudentClassEnrollmentResponseSchema)
def update_student_enrollment(request, enrollment_id: int, payload: StudentClassEnrollmentUpdateSchema):
    """Update an existing student enrollment"""
    from ..models import Class, AcademicSession
    
    enrollment = get_object_or_404(StudentClassEnrollment, id=enrollment_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    if 'student_id' in update_data:
        student = get_object_or_404(Students_Pin_and_ID, id=update_data['student_id'])
        enrollment.student = student
    
    if 'student_class_id' in update_data:
        student_class = get_object_or_404(Class, id=update_data['student_class_id'])
        enrollment.student_class = student_class
    
    if 'academic_session_id' in update_data:
        academic_session = get_object_or_404(AcademicSession, id=update_data['academic_session_id'])
        enrollment.academic_session = academic_session
    
    enrollment.save()
    
    return StudentClassEnrollmentResponseSchema(
        id=enrollment.pk,
        student_name=enrollment.student.student_name if enrollment.student else None,
        class_name=enrollment.student_class.Class if enrollment.student_class else None,
        academic_session=enrollment.academic_session.session if enrollment.academic_session else None
    )


@enrollment_router.delete("/{enrollment_id}", response=StudentClassEnrollmentDeleteSchema)
def delete_student_enrollment(request, enrollment_id: int):
    """Delete a student enrollment"""
    enrollment = get_object_or_404(StudentClassEnrollment, id=enrollment_id)
    enrollment.delete()
    return StudentClassEnrollmentDeleteSchema(deleted_id=enrollment_id)
