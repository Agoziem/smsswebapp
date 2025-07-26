from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route
from typing import List, Optional
from ..models import Attendance
from ..schemas import (
    AttendanceCreateSchema, AttendanceUpdateSchema, AttendanceResponseSchema,
    SuccessResponseSchema
)


@api_controller('/attendance', tags=['Attendance'])
class AttendanceController:
    """Controller for managing teacher attendance"""
    
    @route.get('/', response=List[AttendanceResponseSchema], summary="Get all attendance records")
    def list_attendance(self, teacher_id: Optional[int] = None):
        """Get all attendance records, optionally filter by teacher"""
        queryset = Attendance.objects.all()
        if teacher_id is not None:
            queryset = queryset.filter(teacher_id=teacher_id)
        return queryset
    
    @route.get('/{int:id}', response=AttendanceResponseSchema, summary="Get attendance by ID")
    def get_attendance(self, id: int):
        """Get a specific attendance record by ID"""
        return get_object_or_404(Attendance, id=id)
    
    @route.post('/', response=AttendanceResponseSchema, summary="Create new attendance record")
    def create_attendance(self, payload: AttendanceCreateSchema):
        """Create a new attendance record"""
        return Attendance.objects.create(**payload.model_dump())
    
    @route.put('/{int:id}', response=AttendanceResponseSchema, summary="Update attendance record")
    def update_attendance(self, id: int, payload: AttendanceUpdateSchema):
        """Update an existing attendance record"""
        attendance = get_object_or_404(Attendance, id=id)
        for attr, value in payload.model_dump(exclude_unset=True).items():
            setattr(attendance, attr, value)
        attendance.save()
        return attendance
    
    @route.delete('/{int:id}', response=SuccessResponseSchema, summary="Delete attendance record")
    def delete_attendance(self, id: int):
        """Delete an attendance record"""
        attendance = get_object_or_404(Attendance, id=id)
        attendance.delete()
        return {"message": "Attendance record deleted successfully"}
