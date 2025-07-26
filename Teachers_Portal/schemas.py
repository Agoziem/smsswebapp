from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional, List
from datetime import datetime, date
from datetime import date as date_type


# Teacher Schemas
class TeacherBase(BaseModel):
    first_name: str = Field(default="None", max_length=200, description="Teacher first name")
    last_name: str = Field(default="None", max_length=200, description="Teacher last name")
    phone_number: str = Field(..., max_length=200, description="Phone number")
    email: EmailStr = Field(..., max_length=200, description="Email address")
    role: str = Field(default="Teacher", max_length=200, description="Teacher role")


class TeacherCreateSchema(TeacherBase):
    """Schema for creating a new teacher"""
    user_id: int = Field(..., description="User ID")
    subjects_taught_ids: List[int] = Field(default_factory=list, description="List of subject IDs taught")
    classes_taught_ids: List[int] = Field(default_factory=list, description="List of class IDs taught")
    class_formed_id: Optional[int] = Field(None, description="Class formed ID")
    headshot: Optional[str] = Field(None, description="Teacher headshot image")


class TeacherUpdateSchema(BaseModel):
    """Schema for updating a teacher"""
    user_id: Optional[int] = Field(None, description="User ID")
    first_name: Optional[str] = Field(None, max_length=200, description="Teacher first name")
    last_name: Optional[str] = Field(None, max_length=200, description="Teacher last name")
    phone_number: Optional[str] = Field(None, max_length=200, description="Phone number")
    email: Optional[EmailStr] = Field(None, max_length=200, description="Email address")
    role: Optional[str] = Field(None, max_length=200, description="Teacher role")
    subjects_taught_ids: Optional[List[int]] = Field(None, description="List of subject IDs taught")
    classes_taught_ids: Optional[List[int]] = Field(None, description="List of class IDs taught")
    class_formed_id: Optional[int] = Field(None, description="Class formed ID")
    headshot: Optional[str] = Field(None, description="Teacher headshot image")


class TeacherResponseSchema(TeacherBase):
    """Schema for teacher response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    teachers_id: Optional[str] = Field(None, description="Teacher ID")
    user_id: Optional[int] = Field(None, description="User ID")
    username: Optional[str] = Field(None, description="Username")
    subjects_taught: List[str] = Field(default_factory=list, description="List of subjects taught")
    classes_taught: List[str] = Field(default_factory=list, description="List of classes taught")
    class_formed: Optional[str] = Field(None, description="Class formed")
    headshot_url: Optional[str] = Field(None, description="Teacher headshot URL")


class TeacherDeleteSchema(BaseModel):
    """Schema for teacher deletion confirmation"""
    message: str = Field(default="Teacher deleted successfully")
    deleted_id: int


# Attendance Schemas
class AttendanceBase(BaseModel):
    date: date_type = Field(..., description="Attendance date")
    is_present: bool = Field(default=False, description="Is student present")


class AttendanceCreateSchema(AttendanceBase):
    """Schema for creating new attendance"""
    student_id: int = Field(..., description="Student ID")
    teacher_id: int = Field(..., description="Teacher ID")


class AttendanceUpdateSchema(BaseModel):
    """Schema for updating attendance"""
    student_id: Optional[int] = Field(None, description="Student ID")
    teacher_id: Optional[int] = Field(None, description="Teacher ID")
    date: Optional[date_type] = Field(None, description="Attendance date")
    is_present: Optional[bool] = Field(None, description="Is student present")


class AttendanceResponseSchema(AttendanceBase):
    """Schema for attendance response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    teacher_name: Optional[str] = Field(None, description="Teacher name")
    deleted_at: Optional[datetime] = Field(None, description="Deleted timestamp")


class AttendanceDeleteSchema(BaseModel):
    """Schema for attendance deletion confirmation"""
    message: str = Field(default="Attendance record deleted successfully")
    deleted_id: int