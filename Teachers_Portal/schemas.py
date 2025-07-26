from ninja import ModelSchema, Schema
from typing import Optional, List
from .models import Teacher, Attendance


# Success Response Schema
class SuccessResponseSchema(Schema):
    message: str


# Teacher Schemas
class TeacherCreateSchema(Schema):
    """Schema for creating a new teacher"""
    user_id: int
    FirstName: str
    LastName: str
    Phone_number: Optional[str] = None
    Email: Optional[str] = None
    Role: Optional[str] = "Teacher"
    subject_ids: Optional[List[int]] = None
    class_ids: Optional[List[int]] = None
    classFormed_id: Optional[int] = None
    Headshot: Optional[str] = None


class TeacherUpdateSchema(Schema):
    """Schema for updating a teacher"""
    user_id: Optional[int] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone_number: Optional[str] = None
    Email: Optional[str] = None
    Role: Optional[str] = None
    subject_ids: Optional[List[int]] = None
    class_ids: Optional[List[int]] = None
    classFormed_id: Optional[int] = None
    Headshot: Optional[str] = None


class TeacherResponseSchema(ModelSchema):
    """Schema for teacher response"""
    class Meta:
        model = Teacher
        fields = '__all__'


# Attendance Schemas
class AttendanceCreateSchema(Schema):
    """Schema for creating a new attendance record"""
    student_id: int
    date: str  # YYYY-MM-DD format
    Teacher_id: int
    is_present: bool = False


class AttendanceUpdateSchema(Schema):
    """Schema for updating an attendance record"""
    student_id: Optional[int] = None
    date: Optional[str] = None  # YYYY-MM-DD format
    Teacher_id: Optional[int] = None
    is_present: Optional[bool] = None


class AttendanceResponseSchema(ModelSchema):
    """Schema for attendance response"""
    class Meta:
        model = Attendance
        fields = '__all__'