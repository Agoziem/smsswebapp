from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional


# School Schemas
class SchoolBase(BaseModel):
    school_id: int = Field(..., description="School ID")
    school_name: str = Field(..., max_length=300, description="School name")
    school_phone_number: str = Field(..., max_length=300, description="School phone number")
    school_motto: str = Field(..., max_length=300, description="School motto")
    school_location: str = Field(..., max_length=300, description="School location")
    facebook_page: str = Field(..., max_length=300, description="Facebook page")
    twitter_page: str = Field(..., max_length=300, description="Twitter page")
    whatsapp: str = Field(..., max_length=300, description="WhatsApp number")
    email_address: str = Field(..., max_length=300, description="Email address")


class SchoolCreateSchema(SchoolBase):
    """Schema for creating a new school"""
    school_logo: Optional[str] = Field(None, description="School logo image")


class SchoolUpdateSchema(BaseModel):
    """Schema for updating a school"""
    school_id: Optional[int] = Field(None, description="School ID")
    school_name: Optional[str] = Field(None, max_length=300, description="School name")
    school_phone_number: Optional[str] = Field(None, max_length=300, description="School phone number")
    school_motto: Optional[str] = Field(None, max_length=300, description="School motto")
    school_location: Optional[str] = Field(None, max_length=300, description="School location")
    facebook_page: Optional[str] = Field(None, max_length=300, description="Facebook page")
    twitter_page: Optional[str] = Field(None, max_length=300, description="Twitter page")
    whatsapp: Optional[str] = Field(None, max_length=300, description="WhatsApp number")
    email_address: Optional[str] = Field(None, max_length=300, description="Email address")
    school_logo: Optional[str] = Field(None, description="School logo image")


class SchoolResponseSchema(SchoolBase):
    """Schema for school response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    school_logo: Optional[str] = Field(None, description="School logo URL")


class SchoolDeleteSchema(BaseModel):
    """Schema for school deletion confirmation"""
    message: str = Field(default="School deleted successfully")
    deleted_id: int


# Management Schemas
class ManagementBase(BaseModel):
    profile_name: str = Field(..., max_length=300, description="Profile name")
    role: str = Field(..., max_length=300, description="Role")
    phone_number: str = Field(..., max_length=300, description="Phone number")
    email_address: str = Field(..., max_length=300, description="Email address")
    facebook_page: str = Field(..., max_length=300, description="Facebook page")
    twitter_page: str = Field(..., max_length=300, description="Twitter page")
    whatsapp: str = Field(..., max_length=300, description="WhatsApp number")


class ManagementCreateSchema(ManagementBase):
    """Schema for creating a new management profile"""
    profile_image: Optional[str] = Field(None, description="Profile image")


class ManagementUpdateSchema(BaseModel):
    """Schema for updating a management profile"""
    profile_name: Optional[str] = Field(None, max_length=300, description="Profile name")
    role: Optional[str] = Field(None, max_length=300, description="Role")
    phone_number: Optional[str] = Field(None, max_length=300, description="Phone number")
    email_address: Optional[str] = Field(None, max_length=300, description="Email address")
    facebook_page: Optional[str] = Field(None, max_length=300, description="Facebook page")
    twitter_page: Optional[str] = Field(None, max_length=300, description="Twitter page")
    whatsapp: Optional[str] = Field(None, max_length=300, description="WhatsApp number")
    profile_image: Optional[str] = Field(None, description="Profile image")


class ManagementResponseSchema(ManagementBase):
    """Schema for management response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    profile_image: Optional[str] = Field(None, description="Profile image URL")


class ManagementDeleteSchema(BaseModel):
    """Schema for management deletion confirmation"""
    message: str = Field(default="Management profile deleted successfully")
    deleted_id: int


# TopTeacher Schemas
class TopTeacherBase(BaseModel):
    profile_name: str = Field(..., max_length=300, description="Profile name")
    role: str = Field(..., max_length=300, description="Role")
    phone_number: str = Field(..., max_length=300, description="Phone number")
    email_address: str = Field(..., max_length=300, description="Email address")
    facebook_page: str = Field(..., max_length=300, description="Facebook page")
    twitter_page: str = Field(..., max_length=300, description="Twitter page")
    whatsapp: str = Field(..., max_length=300, description="WhatsApp number")


class TopTeacherCreateSchema(TopTeacherBase):
    """Schema for creating a new top teacher profile"""
    profile_image: Optional[str] = Field(None, description="Profile image")


class TopTeacherUpdateSchema(BaseModel):
    """Schema for updating a top teacher profile"""
    profile_name: Optional[str] = Field(None, max_length=300, description="Profile name")
    role: Optional[str] = Field(None, max_length=300, description="Role")
    phone_number: Optional[str] = Field(None, max_length=300, description="Phone number")
    email_address: Optional[str] = Field(None, max_length=300, description="Email address")
    facebook_page: Optional[str] = Field(None, max_length=300, description="Facebook page")
    twitter_page: Optional[str] = Field(None, max_length=300, description="Twitter page")
    whatsapp: Optional[str] = Field(None, max_length=300, description="WhatsApp number")
    profile_image: Optional[str] = Field(None, description="Profile image")


class TopTeacherResponseSchema(TopTeacherBase):
    """Schema for top teacher response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    profile_image: Optional[str] = Field(None, description="Profile image URL")


class TopTeacherDeleteSchema(BaseModel):
    """Schema for top teacher deletion confirmation"""
    message: str = Field(default="Top teacher profile deleted successfully")
    deleted_id: int


# Subscription Schemas
class SubscriptionBase(BaseModel):
    email: EmailStr = Field(..., description="Email address")


class SubscriptionCreateSchema(SubscriptionBase):
    """Schema for creating a new subscription"""
    pass


class SubscriptionUpdateSchema(BaseModel):
    """Schema for updating a subscription"""
    email: Optional[EmailStr] = Field(None, description="Email address")


class SubscriptionResponseSchema(SubscriptionBase):
    """Schema for subscription response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class SubscriptionDeleteSchema(BaseModel):
    """Schema for subscription deletion confirmation"""
    message: str = Field(default="Subscription deleted successfully")
    deleted_id: int


# Header Schemas
class HeaderBase(BaseModel):
    about: Optional[str] = Field(None, description="About content")
    aims_and_objectives: Optional[str] = Field(None, description="Aims and objectives content")
    vision: Optional[str] = Field(None, description="Vision statement")
    mission: Optional[str] = Field(None, description="Mission statement")


class HeaderCreateSchema(HeaderBase):
    """Schema for creating a new header"""
    pass


class HeaderUpdateSchema(BaseModel):
    """Schema for updating a header"""
    about: Optional[str] = Field(None, description="About content")
    aims_and_objectives: Optional[str] = Field(None, description="Aims and objectives content")
    vision: Optional[str] = Field(None, description="Vision statement")
    mission: Optional[str] = Field(None, description="Mission statement")


class HeaderResponseSchema(HeaderBase):
    """Schema for header response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    snippet: Optional[str] = Field(None, description="About snippet")


class HeaderDeleteSchema(BaseModel):
    """Schema for header deletion confirmation"""
    message: str = Field(default="Header deleted successfully")
    deleted_id: int


# PhotoGallery Schemas
class PhotoGalleryBase(BaseModel):
    description: str = Field(..., max_length=300, description="Photo description")


class PhotoGalleryCreateSchema(PhotoGalleryBase):
    """Schema for creating a new photo gallery item"""
    photo: str = Field(..., description="Photo file")


class PhotoGalleryUpdateSchema(BaseModel):
    """Schema for updating a photo gallery item"""
    description: Optional[str] = Field(None, max_length=300, description="Photo description")
    photo: Optional[str] = Field(None, description="Photo file")


class PhotoGalleryResponseSchema(PhotoGalleryBase):
    """Schema for photo gallery response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    photo: Optional[str] = Field(None, description="Photo URL")


class PhotoGalleryDeleteSchema(BaseModel):
    """Schema for photo gallery deletion confirmation"""
    message: str = Field(default="Photo gallery item deleted successfully")
    deleted_id: int


# UpcomingEvents Schemas
class UpcomingEventsBase(BaseModel):
    event_title: str = Field(..., max_length=300, description="Event title")
    event_topic: str = Field(..., max_length=300, description="Event topic")
    event_speaker_chairman: str = Field(..., max_length=300, description="Event speaker/chairman")
    event_date: str = Field(..., max_length=300, description="Event date")
    event_time: str = Field(..., max_length=300, description="Event time")
    event_venue: str = Field(..., max_length=300, description="Event venue")


class UpcomingEventsCreateSchema(UpcomingEventsBase):
    """Schema for creating a new upcoming event"""
    flier: Optional[str] = Field(None, description="Event flier")


class UpcomingEventsUpdateSchema(BaseModel):
    """Schema for updating an upcoming event"""
    event_title: Optional[str] = Field(None, max_length=300, description="Event title")
    event_topic: Optional[str] = Field(None, max_length=300, description="Event topic")
    event_speaker_chairman: Optional[str] = Field(None, max_length=300, description="Event speaker/chairman")
    event_date: Optional[str] = Field(None, max_length=300, description="Event date")
    event_time: Optional[str] = Field(None, max_length=300, description="Event time")
    event_venue: Optional[str] = Field(None, max_length=300, description="Event venue")
    flier: Optional[str] = Field(None, description="Event flier")


class UpcomingEventsResponseSchema(UpcomingEventsBase):
    """Schema for upcoming events response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    flier: Optional[str] = Field(None, description="Event flier URL")


class UpcomingEventsDeleteSchema(BaseModel):
    """Schema for upcoming events deletion confirmation"""
    message: str = Field(default="Upcoming event deleted successfully")
    deleted_id: int


# FAQ Schemas
class FAQBase(BaseModel):
    question_number: str = Field(..., max_length=300, description="Question number")
    questions: str = Field(..., max_length=300, description="Questions")
    answer: str = Field(..., max_length=300, description="Answer")


class FAQCreateSchema(FAQBase):
    """Schema for creating a new FAQ"""
    pass


class FAQUpdateSchema(BaseModel):
    """Schema for updating a FAQ"""
    question_number: Optional[str] = Field(None, max_length=300, description="Question number")
    questions: Optional[str] = Field(None, max_length=300, description="Questions")
    answer: Optional[str] = Field(None, max_length=300, description="Answer")


class FAQResponseSchema(FAQBase):
    """Schema for FAQ response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class FAQDeleteSchema(BaseModel):
    """Schema for FAQ deletion confirmation"""
    message: str = Field(default="FAQ deleted successfully")
    deleted_id: int


# Contact Schemas
class ContactBase(BaseModel):
    name: str = Field(..., max_length=100, description="Contact name")
    message: str = Field(..., max_length=80, description="Contact message")
    email: EmailStr = Field(..., description="Contact email")


class ContactCreateSchema(ContactBase):
    """Schema for creating a new contact"""
    pass


class ContactUpdateSchema(BaseModel):
    """Schema for updating a contact"""
    name: Optional[str] = Field(None, max_length=100, description="Contact name")
    message: Optional[str] = Field(None, max_length=80, description="Contact message")
    email: Optional[EmailStr] = Field(None, description="Contact email")


class ContactResponseSchema(ContactBase):
    """Schema for contact response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ContactDeleteSchema(BaseModel):
    """Schema for contact deletion confirmation"""
    message: str = Field(default="Contact deleted successfully")
    deleted_id: int


# ParentsReview Schemas
class ParentsReviewBase(BaseModel):
    name: str = Field(..., max_length=300, description="Parent name")
    occupation: str = Field(..., max_length=300, description="Parent occupation")
    review: str = Field(..., description="Parent review")


class ParentsReviewCreateSchema(ParentsReviewBase):
    """Schema for creating a new parent review"""
    profile_image: Optional[str] = Field(None, description="Profile image")


class ParentsReviewUpdateSchema(BaseModel):
    """Schema for updating a parent review"""
    name: Optional[str] = Field(None, max_length=300, description="Parent name")
    occupation: Optional[str] = Field(None, max_length=300, description="Parent occupation")
    review: Optional[str] = Field(None, description="Parent review")
    profile_image: Optional[str] = Field(None, description="Profile image")


class ParentsReviewResponseSchema(ParentsReviewBase):
    """Schema for parent review response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    profile_image: Optional[str] = Field(None, description="Profile image URL")


class ParentsReviewDeleteSchema(BaseModel):
    """Schema for parent review deletion confirmation"""
    message: str = Field(default="Parent review deleted successfully")
    deleted_id: int