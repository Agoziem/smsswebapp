from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import School
from ..schemas import (
    SchoolCreateSchema,
    SchoolUpdateSchema,
    SchoolResponseSchema,
    SchoolDeleteSchema
)

router = Router(tags=["School"])


@router.get("/", response=List[SchoolResponseSchema])
def list_schools(request):
    """Get all schools"""
    schools = School.objects.all()
    return [
        SchoolResponseSchema(
            id=school.pk,
            school_id=school.Schoolid,
            school_name=school.Schoolname,
            school_phone_number=school.SchoolPhonenumber,
            school_motto=school.Schoolmotto,
            school_location=school.Schoollocation,
            facebook_page=school.Facebookpage,
            twitter_page=school.Twitterpage,
            whatsapp=school.Whatsapp,
            email_address=school.Emailaddress,
            school_logo=school.imageURL
        ) for school in schools
    ]


@router.get("/{school_id}", response=SchoolResponseSchema)
def get_school(request, school_id: int):
    """Get a specific school by ID"""
    school = get_object_or_404(School, id=school_id)
    return SchoolResponseSchema(
        id=school.pk,
        school_id=school.Schoolid,
        school_name=school.Schoolname,
        school_phone_number=school.SchoolPhonenumber,
        school_motto=school.Schoolmotto,
        school_location=school.Schoollocation,
        facebook_page=school.Facebookpage,
        twitter_page=school.Twitterpage,
        whatsapp=school.Whatsapp,
        email_address=school.Emailaddress,
        school_logo=school.imageURL
    )


@router.post("/", response=SchoolResponseSchema)
def create_school(request, payload: SchoolCreateSchema):
    """Create a new school"""
    school = School.objects.create(
        Schoolid=payload.school_id,
        Schoolname=payload.school_name,
        SchoolPhonenumber=payload.school_phone_number,
        Schoolmotto=payload.school_motto,
        Schoollocation=payload.school_location,
        Facebookpage=payload.facebook_page,
        Twitterpage=payload.twitter_page,
        Whatsapp=payload.whatsapp,
        Emailaddress=payload.email_address,
        Schoollogo=payload.school_logo
    )
    
    return SchoolResponseSchema(
        id=school.pk,
        school_id=school.Schoolid,
        school_name=school.Schoolname,
        school_phone_number=school.SchoolPhonenumber,
        school_motto=school.Schoolmotto,
        school_location=school.Schoollocation,
        facebook_page=school.Facebookpage,
        twitter_page=school.Twitterpage,
        whatsapp=school.Whatsapp,
        email_address=school.Emailaddress,
        school_logo=school.imageURL
    )


@router.put("/{school_id}", response=SchoolResponseSchema)
def update_school(request, school_id: int, payload: SchoolUpdateSchema):
    """Update an existing school"""
    school = get_object_or_404(School, id=school_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'school_id': 'Schoolid',
        'school_name': 'Schoolname',
        'school_phone_number': 'SchoolPhonenumber',
        'school_motto': 'Schoolmotto',
        'school_location': 'Schoollocation',
        'facebook_page': 'Facebookpage',
        'twitter_page': 'Twitterpage',
        'whatsapp': 'Whatsapp',
        'email_address': 'Emailaddress',
        'school_logo': 'Schoollogo'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(school, model_field, value)
    
    school.save()
    
    return SchoolResponseSchema(
        id=school.pk,
        school_id=school.Schoolid,
        school_name=school.Schoolname,
        school_phone_number=school.SchoolPhonenumber,
        school_motto=school.Schoolmotto,
        school_location=school.Schoollocation,
        facebook_page=school.Facebookpage,
        twitter_page=school.Twitterpage,
        whatsapp=school.Whatsapp,
        email_address=school.Emailaddress,
        school_logo=school.imageURL
    )


@router.delete("/{school_id}", response=SchoolDeleteSchema)
def delete_school(request, school_id: int):
    """Delete a school"""
    school = get_object_or_404(School, id=school_id)
    school.delete()
    return SchoolDeleteSchema(deleted_id=school_id)
