from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Attendance, Teacher
from Result_portal.models import Students_Pin_and_ID
from ..schemas import (
    AttendanceCreateSchema,
    AttendanceUpdateSchema,
    AttendanceResponseSchema,
    AttendanceDeleteSchema
)

router = Router(tags=["Attendance"])


@router.get("/", response=List[AttendanceResponseSchema])
def list_attendance(request):
    """Get all attendance records"""
    attendance_records = Attendance.objects.select_related('student', 'Teacher').all()
    return [
        AttendanceResponseSchema(
            id=attendance.pk,
            date=attendance.date,
            is_present=attendance.is_present,
            student_name=attendance.student.student_name if attendance.student else None,
            teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else None,
            deleted_at=attendance.deleted_at
        ) for attendance in attendance_records
    ]


@router.get("/{attendance_id}", response=AttendanceResponseSchema)
def get_attendance(request, attendance_id: int):
    """Get a specific attendance record by ID"""
    attendance = get_object_or_404(
        Attendance.objects.select_related('student', 'Teacher'),
        id=attendance_id
    )
    return AttendanceResponseSchema(
        id=attendance.pk,
        date=attendance.date,
        is_present=attendance.is_present,
        student_name=attendance.student.student_name if attendance.student else None,
        teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else None,
        deleted_at=attendance.deleted_at
    )


@router.post("/", response=AttendanceResponseSchema)
def create_attendance(request, payload: AttendanceCreateSchema):
    """Create a new attendance record"""
    student = get_object_or_404(Students_Pin_and_ID, id=payload.student_id)
    teacher = get_object_or_404(Teacher, id=payload.teacher_id)
    
    attendance = Attendance.objects.create(
        student=student,
        Teacher=teacher,
        date=payload.date,
        is_present=payload.is_present
    )
    
    return AttendanceResponseSchema(
        id=attendance.pk,
        date=attendance.date,
        is_present=attendance.is_present,
        student_name=attendance.student.student_name if attendance.student else "Not Available",
        teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else "Not Available",
        deleted_at=attendance.deleted_at
    )


@router.put("/{attendance_id}", response=AttendanceResponseSchema)
def update_attendance(request, attendance_id: int, payload: AttendanceUpdateSchema):
    """Update an existing attendance record"""
    attendance = get_object_or_404(Attendance, id=attendance_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    # Update foreign keys
    if 'student_id' in update_data:
        student = get_object_or_404(Students_Pin_and_ID, id=update_data['student_id'])
        attendance.student = student
    
    if 'teacher_id' in update_data:
        teacher = get_object_or_404(Teacher, id=update_data['teacher_id'])
        attendance.Teacher = teacher
    
    # Update other fields
    if 'date' in update_data:
        attendance.date = update_data['date']
    
    if 'is_present' in update_data:
        attendance.is_present = update_data['is_present']
    
    attendance.save()
    
    return AttendanceResponseSchema(
        id=attendance.pk,
        date=attendance.date,
        is_present=attendance.is_present,
        student_name=attendance.student.student_name if attendance.student else None,
        teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else None,
        deleted_at=attendance.deleted_at
    )


@router.delete("/{attendance_id}", response=AttendanceDeleteSchema)
def delete_attendance(request, attendance_id: int):
    """Delete an attendance record"""
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.delete()
    return AttendanceDeleteSchema(deleted_id=attendance_id)


# Bulk attendance endpoints
@router.post("/bulk/", response=List[AttendanceResponseSchema])
def create_bulk_attendance(request, payload: List[AttendanceCreateSchema]):
    """Create multiple attendance records at once"""
    attendance_records = []
    
    for attendance_data in payload:
        student = get_object_or_404(Students_Pin_and_ID, id=attendance_data.student_id)
        teacher = get_object_or_404(Teacher, id=attendance_data.teacher_id)
        
        attendance = Attendance.objects.create(
            student=student,
            Teacher=teacher,
            date=attendance_data.date,
            is_present=attendance_data.is_present
        )
        attendance_records.append(attendance)
    
    return [
        AttendanceResponseSchema(
            id=attendance.id,
            date=attendance.date,
            is_present=attendance.is_present,
            student_name=attendance.student.student_name,
            teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}",
            deleted_at=attendance.deleted_at
        ) for attendance in attendance_records
    ]


@router.get("/by-date/{date}", response=List[AttendanceResponseSchema])
def get_attendance_by_date(request, date: str):
    """Get attendance records for a specific date"""
    from datetime import datetime
    
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HttpError(400, "Invalid date format. Use YYYY-MM-DD")
    
    attendance_records = Attendance.objects.filter(date=date_obj).select_related('student', 'Teacher')
    
    return [
        AttendanceResponseSchema(
            id=attendance.pk,
            date=attendance.date,
            is_present=attendance.is_present,
            student_name=attendance.student.student_name if attendance.student else None,
            teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else None,
            deleted_at=attendance.deleted_at
        ) for attendance in attendance_records
    ]


@router.get("/by-student/{student_id}", response=List[AttendanceResponseSchema])
def get_attendance_by_student(request, student_id: int):
    """Get attendance records for a specific student"""
    student = get_object_or_404(Students_Pin_and_ID, id=student_id)
    attendance_records = Attendance.objects.filter(student=student).select_related('student', 'Teacher')
    
    return [
        AttendanceResponseSchema(
            id=attendance.pk,
            date=attendance.date,
            is_present=attendance.is_present,
            student_name=attendance.student.student_name if attendance.student else "Not Available",
            teacher_name=f"{attendance.Teacher.FirstName} {attendance.Teacher.LastName}" if attendance.Teacher else "Not Available",
            deleted_at=attendance.deleted_at
        ) for attendance in attendance_records
    ]
