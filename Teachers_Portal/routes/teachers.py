from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from typing import List

from ..models import Teacher
from Result_portal.models import Subject, Class
from ..schemas import (
    TeacherCreateSchema,
    TeacherUpdateSchema,
    TeacherResponseSchema,
    TeacherDeleteSchema
)

router = Router(tags=["Teachers"])


@router.get("/", response=List[TeacherResponseSchema])
def list_teachers(request):
    """Get all teachers"""
    teachers = Teacher.objects.select_related('user', 'classFormed').prefetch_related('subjects_taught', 'classes_taught').all()
    return [
        TeacherResponseSchema(
            id=teacher.pk,
            first_name=teacher.FirstName,
            last_name=teacher.LastName,
            phone_number=teacher.Phone_number,
            email=teacher.Email,
            teachers_id=teacher.teachers_id,
            role=teacher.Role,
            user_id=teacher.user.pk if teacher.user else None,
            username=teacher.user.username if teacher.user else None,
            subjects_taught=[subject.subject_name for subject in teacher.subjects_taught.all()],
            classes_taught=[cls.Class for cls in teacher.classes_taught.all()],
            class_formed=teacher.classFormed.Class if teacher.classFormed else None,
            headshot_url=teacher.profileimageURL
        ) for teacher in teachers
    ]


@router.get("/{teacher_id}", response=TeacherResponseSchema)
def get_teacher(request, teacher_id: int):
    """Get a specific teacher by ID"""
    teacher = get_object_or_404(
        Teacher.objects.select_related('user', 'classFormed').prefetch_related('subjects_taught', 'classes_taught'),
        id=teacher_id
    )
    return TeacherResponseSchema(
        id=teacher.pk,
        first_name=teacher.FirstName,
        last_name=teacher.LastName,
        phone_number=teacher.Phone_number,
        email=teacher.Email,
        teachers_id=teacher.teachers_id,
        role=teacher.Role,
        user_id=teacher.user.pk if teacher.user else None,
        username=teacher.user.username if teacher.user else None,
        subjects_taught=[subject.subject_name for subject in teacher.subjects_taught.all()],
        classes_taught=[cls.Class for cls in teacher.classes_taught.all()],
        class_formed=teacher.classFormed.Class if teacher.classFormed else None,
        headshot_url=teacher.profileimageURL
    )


@router.post("/", response=TeacherResponseSchema)
def create_teacher(request, payload: TeacherCreateSchema):
    """Create a new teacher"""
    # Get the user
    user = get_object_or_404(User, id=payload.user_id)
    
    # Create teacher
    teacher = Teacher.objects.create(
        user=user,
        FirstName=payload.first_name,
        LastName=payload.last_name,
        Phone_number=payload.phone_number,
        Email=payload.email,
        Role=payload.role,
        Headshot=payload.headshot
    )
    
    # Add subjects taught
    if payload.subjects_taught_ids:
        subjects = Subject.objects.filter(id__in=payload.subjects_taught_ids)
        teacher.subjects_taught.set(subjects)
    
    # Add classes taught
    if payload.classes_taught_ids:
        classes = Class.objects.filter(id__in=payload.classes_taught_ids)
        teacher.classes_taught.set(classes)
    
    # Set class formed
    if payload.class_formed_id:
        class_formed = get_object_or_404(Class, id=payload.class_formed_id)
        teacher.classFormed = class_formed
        teacher.save()
    
    return TeacherResponseSchema(
        id=teacher.pk,
        first_name=teacher.FirstName,
        last_name=teacher.LastName,
        phone_number=teacher.Phone_number,
        email=teacher.Email,
        teachers_id=teacher.teachers_id,
        role=teacher.Role,
        user_id=teacher.user.pk if teacher.user else None,
        username=teacher.user.username if teacher.user else None,
        subjects_taught=[subject.subject_name for subject in teacher.subjects_taught.all()],
        classes_taught=[cls.Class for cls in teacher.classes_taught.all()],
        class_formed=teacher.classFormed.Class if teacher.classFormed else None,
        headshot_url=teacher.profileimageURL
    )


@router.put("/{teacher_id}", response=TeacherResponseSchema)
def update_teacher(request, teacher_id: int, payload: TeacherUpdateSchema):
    """Update an existing teacher"""
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    # Update user if provided
    if 'user_id' in update_data:
        user = get_object_or_404(User, id=update_data['user_id'])
        teacher.user = user
    
    # Update basic fields
    field_mapping = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'phone_number': 'Phone_number',
        'email': 'Email',
        'role': 'Role',
        'headshot': 'Headshot'
    }
    
    for key, value in update_data.items():
        if key in field_mapping:
            setattr(teacher, field_mapping[key], value)
    
    # Update many-to-many relationships
    if 'subjects_taught_ids' in update_data:
        subjects = Subject.objects.filter(id__in=update_data['subjects_taught_ids'])
        teacher.subjects_taught.set(subjects)
    
    if 'classes_taught_ids' in update_data:
        classes = Class.objects.filter(id__in=update_data['classes_taught_ids'])
        teacher.classes_taught.set(classes)
    
    # Update class formed
    if 'class_formed_id' in update_data:
        if update_data['class_formed_id']:
            class_formed = get_object_or_404(Class, id=update_data['class_formed_id'])
            teacher.classFormed = class_formed
        else:
            teacher.classFormed = None
    
    teacher.save()
    
    return TeacherResponseSchema(
        id=teacher.pk,
        first_name=teacher.FirstName,
        last_name=teacher.LastName,
        phone_number=teacher.Phone_number,
        email=teacher.Email,
        teachers_id=teacher.teachers_id,
        role=teacher.Role,
        user_id=teacher.user.pk if teacher.user else None,
        username=teacher.user.username if teacher.user else None,
        subjects_taught=[subject.subject_name for subject in teacher.subjects_taught.all()],
        classes_taught=[cls.Class for cls in teacher.classes_taught.all()],
        class_formed=teacher.classFormed.Class if teacher.classFormed else None,
        headshot_url=teacher.profileimageURL
    )


@router.delete("/{teacher_id}", response=TeacherDeleteSchema)
def delete_teacher(request, teacher_id: int):
    """Delete a teacher"""
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return TeacherDeleteSchema(deleted_id=teacher_id)
