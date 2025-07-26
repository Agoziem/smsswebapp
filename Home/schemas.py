from ninja import ModelSchema, Schema
from typing import Optional
from .models import (
    School, Management, TopTeacher, Subscription, Header, 
    PhotoGallery, UpcomingEvents, FAQ, Contact, ParentsReview
)


# Success Response Schema
class SuccessResponseSchema(Schema):
    message: str


# School Schemas
class SchoolCreateSchema(Schema):
    """Schema for creating a new school"""
    Schoolid: int
    Schoolname: str
    SchoolPhonenumber: str
    Schoolmotto: str
    Schoollocation: str
    Facebookpage: str
    Twitterpage: str
    Whatsapp: str
    Emailaddress: str
    Schoollogo: Optional[str] = None


class SchoolUpdateSchema(Schema):
    """Schema for updating a school"""
    Schoolid: Optional[int] = None
    Schoolname: Optional[str] = None
    SchoolPhonenumber: Optional[str] = None
    Schoolmotto: Optional[str] = None
    Schoollocation: Optional[str] = None
    Facebookpage: Optional[str] = None
    Twitterpage: Optional[str] = None
    Whatsapp: Optional[str] = None
    Emailaddress: Optional[str] = None
    Schoollogo: Optional[str] = None


class SchoolResponseSchema(ModelSchema):
    """Schema for school response"""
    class Meta:
        model = School
        fields = '__all__'


# Management Schemas
class ManagementCreateSchema(Schema):
    """Schema for creating management profile"""
    Profilename: str
    Role: str
    Phonenumber: str
    Emailaddress: str
    Facebookpage: str
    Twitterpage: str
    Whatsapp: str
    Profileimage: Optional[str] = None


class ManagementUpdateSchema(Schema):
    """Schema for updating management profile"""
    Profilename: Optional[str] = None
    Role: Optional[str] = None
    Phonenumber: Optional[str] = None
    Emailaddress: Optional[str] = None
    Facebookpage: Optional[str] = None
    Twitterpage: Optional[str] = None
    Whatsapp: Optional[str] = None
    Profileimage: Optional[str] = None


class ManagementResponseSchema(ModelSchema):
    """Schema for management response"""
    class Meta:
        model = Management
        fields = '__all__'


# TopTeacher Schemas
class TopTeacherCreateSchema(Schema):
    """Schema for creating top teacher"""
    Profilename: str
    Role: str
    Phonenumber: str
    Emailaddress: str
    Facebookpage: str
    Twitterpage: str
    Whatsapp: str
    Profileimage: Optional[str] = None


class TopTeacherUpdateSchema(Schema):
    """Schema for updating top teacher"""
    Profilename: Optional[str] = None
    Role: Optional[str] = None
    Phonenumber: Optional[str] = None
    Emailaddress: Optional[str] = None
    Facebookpage: Optional[str] = None
    Twitterpage: Optional[str] = None
    Whatsapp: Optional[str] = None
    Profileimage: Optional[str] = None


class TopTeacherResponseSchema(ModelSchema):
    """Schema for top teacher response"""
    class Meta:
        model = TopTeacher
        fields = '__all__'


# Subscription Schemas
class SubscriptionCreateSchema(Schema):
    """Schema for creating subscription"""
    Email: str


class SubscriptionUpdateSchema(Schema):
    """Schema for updating subscription"""
    Email: Optional[str] = None


class SubscriptionResponseSchema(ModelSchema):
    """Schema for subscription response"""
    class Meta:
        model = Subscription
        fields = '__all__'


# Header Schemas
class HeaderCreateSchema(Schema):
    """Schema for creating header"""
    About: Optional[str] = None
    Aims_and_Objectives: Optional[str] = None
    Vision: Optional[str] = None
    Mission: Optional[str] = None


class HeaderUpdateSchema(Schema):
    """Schema for updating header"""
    About: Optional[str] = None
    Aims_and_Objectives: Optional[str] = None
    Vision: Optional[str] = None
    Mission: Optional[str] = None


class HeaderResponseSchema(ModelSchema):
    """Schema for header response"""
    class Meta:
        model = Header
        fields = '__all__'


# PhotoGallery Schemas
class PhotoGalleryCreateSchema(Schema):
    """Schema for creating photo gallery"""
    Description: str
    Photo: Optional[str] = None


class PhotoGalleryUpdateSchema(Schema):
    """Schema for updating photo gallery"""
    Description: Optional[str] = None
    Photo: Optional[str] = None


class PhotoGalleryResponseSchema(ModelSchema):
    """Schema for photo gallery response"""
    class Meta:
        model = PhotoGallery
        fields = '__all__'


# UpcomingEvents Schemas
class UpcomingEventsCreateSchema(Schema):
    """Schema for creating upcoming events"""
    Eventtitle: str
    EventTopic: str
    Eventspeaker_Chairman: str
    Eventdate: str
    Eventtime: str
    Eventvenue: str
    Flier: Optional[str] = None


class UpcomingEventsUpdateSchema(Schema):
    """Schema for updating upcoming events"""
    Eventtitle: Optional[str] = None
    EventTopic: Optional[str] = None
    Eventspeaker_Chairman: Optional[str] = None
    Eventdate: Optional[str] = None
    Eventtime: Optional[str] = None
    Eventvenue: Optional[str] = None
    Flier: Optional[str] = None


class UpcomingEventsResponseSchema(ModelSchema):
    """Schema for upcoming events response"""
    class Meta:
        model = UpcomingEvents
        fields = '__all__'


# FAQ Schemas
class FAQCreateSchema(Schema):
    """Schema for creating FAQ"""
    questionnumber: str
    Questions: str
    Answer: str


class FAQUpdateSchema(Schema):
    """Schema for updating FAQ"""
    questionnumber: Optional[str] = None
    Questions: Optional[str] = None
    Answer: Optional[str] = None


class FAQResponseSchema(ModelSchema):
    """Schema for FAQ response"""
    class Meta:
        model = FAQ
        fields = '__all__'


# Contact Schemas
class ContactCreateSchema(Schema):
    """Schema for creating contact"""
    name: str
    message: str
    email: str


class ContactUpdateSchema(Schema):
    """Schema for updating contact"""
    name: Optional[str] = None
    message: Optional[str] = None
    email: Optional[str] = None


class ContactResponseSchema(ModelSchema):
    """Schema for contact response"""
    class Meta:
        model = Contact
        fields = '__all__'


# ParentsReview Schemas
class ParentsReviewCreateSchema(Schema):
    """Schema for creating parents review"""
    Name: str
    Occupation: str
    Review: str
    Profileimage: Optional[str] = None


class ParentsReviewUpdateSchema(Schema):
    """Schema for updating parents review"""
    Name: Optional[str] = None
    Occupation: Optional[str] = None
    Review: Optional[str] = None
    Profileimage: Optional[str] = None


class ParentsReviewResponseSchema(ModelSchema):
    """Schema for parents review response"""
    class Meta:
        model = ParentsReview
        fields = '__all__'
