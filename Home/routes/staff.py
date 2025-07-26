from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Management, TopTeacher
from ..schemas import (
    ManagementCreateSchema,
    ManagementUpdateSchema,
    ManagementResponseSchema,
    ManagementDeleteSchema,
    TopTeacherCreateSchema,
    TopTeacherUpdateSchema,
    TopTeacherResponseSchema,
    TopTeacherDeleteSchema
)

management_router = Router(tags=["Management"])
top_teacher_router = Router(tags=["Top Teachers"])


# Management routes
@management_router.get("/", response=List[ManagementResponseSchema])
def list_management(request):
    """Get all management profiles"""
    management = Management.objects.all()
    return [
        ManagementResponseSchema(
            id=mgmt.pk,
            profile_name=mgmt.Profilename,
            role=mgmt.Role,
            phone_number=mgmt.Phonenumber,
            email_address=mgmt.Emailaddress,
            facebook_page=mgmt.Facebookpage,
            twitter_page=mgmt.Twitterpage,
            whatsapp=mgmt.Whatsapp,
            profile_image=mgmt.managementimageURL()
        ) for mgmt in management
    ]


@management_router.get("/{management_id}", response=ManagementResponseSchema)
def get_management(request, management_id: int):
    """Get a specific management profile by ID"""
    mgmt = get_object_or_404(Management, id=management_id)
    return ManagementResponseSchema(
        id=mgmt.pk,
        profile_name=mgmt.Profilename,
        role=mgmt.Role,
        phone_number=mgmt.Phonenumber,
        email_address=mgmt.Emailaddress,
        facebook_page=mgmt.Facebookpage,
        twitter_page=mgmt.Twitterpage,
        whatsapp=mgmt.Whatsapp,
        profile_image=mgmt.managementimageURL()
    )


@management_router.post("/", response=ManagementResponseSchema)
def create_management(request, payload: ManagementCreateSchema):
    """Create a new management profile"""
    mgmt = Management.objects.create(
        Profilename=payload.profile_name,
        Role=payload.role,
        Phonenumber=payload.phone_number,
        Emailaddress=payload.email_address,
        Facebookpage=payload.facebook_page,
        Twitterpage=payload.twitter_page,
        Whatsapp=payload.whatsapp,
        Profileimage=payload.profile_image
    )
    
    return ManagementResponseSchema(
        id=mgmt.pk,
        profile_name=mgmt.Profilename,
        role=mgmt.Role,
        phone_number=mgmt.Phonenumber,
        email_address=mgmt.Emailaddress,
        facebook_page=mgmt.Facebookpage,
        twitter_page=mgmt.Twitterpage,
        whatsapp=mgmt.Whatsapp,
        profile_image=mgmt.managementimageURL()
    )


@management_router.put("/{management_id}", response=ManagementResponseSchema)
def update_management(request, management_id: int, payload: ManagementUpdateSchema):
    """Update an existing management profile"""
    mgmt = get_object_or_404(Management, id=management_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'profile_name': 'Profilename',
        'role': 'Role',
        'phone_number': 'Phonenumber',
        'email_address': 'Emailaddress',
        'facebook_page': 'Facebookpage',
        'twitter_page': 'Twitterpage',
        'whatsapp': 'Whatsapp',
        'profile_image': 'Profileimage'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(mgmt, model_field, value)
    
    mgmt.save()
    
    return ManagementResponseSchema(
        id=mgmt.pk,
        profile_name=mgmt.Profilename,
        role=mgmt.Role,
        phone_number=mgmt.Phonenumber,
        email_address=mgmt.Emailaddress,
        facebook_page=mgmt.Facebookpage,
        twitter_page=mgmt.Twitterpage,
        whatsapp=mgmt.Whatsapp,
        profile_image=mgmt.managementimageURL()
    )


@management_router.delete("/{management_id}", response=ManagementDeleteSchema)
def delete_management(request, management_id: int):
    """Delete a management profile"""
    mgmt = get_object_or_404(Management, id=management_id)
    mgmt.delete()
    return ManagementDeleteSchema(deleted_id=management_id)


# Top Teacher routes
@top_teacher_router.get("/", response=List[TopTeacherResponseSchema])
def list_top_teachers(request):
    """Get all top teacher profiles"""
    top_teachers = TopTeacher.objects.all()
    return [
        TopTeacherResponseSchema(
            id=teacher.pk,
            profile_name=teacher.Profilename,
            role=teacher.Role,
            phone_number=teacher.Phonenumber,
            email_address=teacher.Emailaddress,
            facebook_page=teacher.Facebookpage,
            twitter_page=teacher.Twitterpage,
            whatsapp=teacher.Whatsapp,
            profile_image=teacher.TopTeachersimageURL()
        ) for teacher in top_teachers
    ]


@top_teacher_router.get("/{teacher_id}", response=TopTeacherResponseSchema)
def get_top_teacher(request, teacher_id: int):
    """Get a specific top teacher profile by ID"""
    teacher = get_object_or_404(TopTeacher, id=teacher_id)
    return TopTeacherResponseSchema(
        id=teacher.pk,
        profile_name=teacher.Profilename,
        role=teacher.Role,
        phone_number=teacher.Phonenumber,
        email_address=teacher.Emailaddress,
        facebook_page=teacher.Facebookpage,
        twitter_page=teacher.Twitterpage,
        whatsapp=teacher.Whatsapp,
        profile_image=teacher.TopTeachersimageURL()
    )


@top_teacher_router.post("/", response=TopTeacherResponseSchema)
def create_top_teacher(request, payload: TopTeacherCreateSchema):
    """Create a new top teacher profile"""
    teacher = TopTeacher.objects.create(
        Profilename=payload.profile_name,
        Role=payload.role,
        Phonenumber=payload.phone_number,
        Emailaddress=payload.email_address,
        Facebookpage=payload.facebook_page,
        Twitterpage=payload.twitter_page,
        Whatsapp=payload.whatsapp,
        Profileimage=payload.profile_image
    )
    
    return TopTeacherResponseSchema(
        id=teacher.pk,
        profile_name=teacher.Profilename,
        role=teacher.Role,
        phone_number=teacher.Phonenumber,
        email_address=teacher.Emailaddress,
        facebook_page=teacher.Facebookpage,
        twitter_page=teacher.Twitterpage,
        whatsapp=teacher.Whatsapp,
        profile_image=teacher.TopTeachersimageURL()
    )


@top_teacher_router.put("/{teacher_id}", response=TopTeacherResponseSchema)
def update_top_teacher(request, teacher_id: int, payload: TopTeacherUpdateSchema):
    """Update an existing top teacher profile"""
    teacher = get_object_or_404(TopTeacher, id=teacher_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'profile_name': 'Profilename',
        'role': 'Role',
        'phone_number': 'Phonenumber',
        'email_address': 'Emailaddress',
        'facebook_page': 'Facebookpage',
        'twitter_page': 'Twitterpage',
        'whatsapp': 'Whatsapp',
        'profile_image': 'Profileimage'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(teacher, model_field, value)
    
    teacher.save()
    
    return TopTeacherResponseSchema(
        id=teacher.pk,
        profile_name=teacher.Profilename,
        role=teacher.Role,
        phone_number=teacher.Phonenumber,
        email_address=teacher.Emailaddress,
        facebook_page=teacher.Facebookpage,
        twitter_page=teacher.Twitterpage,
        whatsapp=teacher.Whatsapp,
        profile_image=teacher.TopTeachersimageURL()
    )


@top_teacher_router.delete("/{teacher_id}", response=TopTeacherDeleteSchema)
def delete_top_teacher(request, teacher_id: int):
    """Delete a top teacher profile"""
    teacher = get_object_or_404(TopTeacher, id=teacher_id)
    teacher.delete()
    return TopTeacherDeleteSchema(deleted_id=teacher_id)
