from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import PhotoGallery, UpcomingEvents, FAQ, ParentsReview
from ..schemas import (
    PhotoGalleryCreateSchema,
    PhotoGalleryUpdateSchema,
    PhotoGalleryResponseSchema,
    PhotoGalleryDeleteSchema,
    UpcomingEventsCreateSchema,
    UpcomingEventsUpdateSchema,
    UpcomingEventsResponseSchema,
    UpcomingEventsDeleteSchema,
    FAQCreateSchema,
    FAQUpdateSchema,
    FAQResponseSchema,
    FAQDeleteSchema,
    ParentsReviewCreateSchema,
    ParentsReviewUpdateSchema,
    ParentsReviewResponseSchema,
    ParentsReviewDeleteSchema
)

photo_gallery_router = Router(tags=["Photo Gallery"])
upcoming_events_router = Router(tags=["Upcoming Events"])
faq_router = Router(tags=["FAQ"])
parents_review_router = Router(tags=["Parents Reviews"])


# Photo Gallery routes
@photo_gallery_router.get("/", response=List[PhotoGalleryResponseSchema])
def list_photo_gallery(request):
    """Get all photo gallery items"""
    photos = PhotoGallery.objects.all()
    return [
        PhotoGalleryResponseSchema(
            id=photo.pk,
            description=photo.Description,
            photo=photo.imageURL
        ) for photo in photos
    ]


@photo_gallery_router.get("/{photo_id}", response=PhotoGalleryResponseSchema)
def get_photo_gallery_item(request, photo_id: int):
    """Get a specific photo gallery item by ID"""
    photo = get_object_or_404(PhotoGallery, id=photo_id)
    return PhotoGalleryResponseSchema(
        id=photo.pk,
        description=photo.Description,
        photo=photo.imageURL
    )


@photo_gallery_router.post("/", response=PhotoGalleryResponseSchema)
def create_photo_gallery_item(request, payload: PhotoGalleryCreateSchema):
    """Create a new photo gallery item"""
    photo = PhotoGallery.objects.create(
        Description=payload.description,
        Photo=payload.photo
    )
    
    return PhotoGalleryResponseSchema(
        id=photo.pk,
        description=photo.Description,
        photo=photo.imageURL
    )


@photo_gallery_router.put("/{photo_id}", response=PhotoGalleryResponseSchema)
def update_photo_gallery_item(request, photo_id: int, payload: PhotoGalleryUpdateSchema):
    """Update an existing photo gallery item"""
    photo = get_object_or_404(PhotoGallery, id=photo_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'description': 'Description',
        'photo': 'Photo'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(photo, model_field, value)
    
    photo.save()
    
    return PhotoGalleryResponseSchema(
        id=photo.pk,
        description=photo.Description,
        photo=photo.imageURL
    )


@photo_gallery_router.delete("/{photo_id}", response=PhotoGalleryDeleteSchema)
def delete_photo_gallery_item(request, photo_id: int):
    """Delete a photo gallery item"""
    photo = get_object_or_404(PhotoGallery, id=photo_id)
    photo.delete()
    return PhotoGalleryDeleteSchema(deleted_id=photo_id)


# Upcoming Events routes
@upcoming_events_router.get("/", response=List[UpcomingEventsResponseSchema])
def list_upcoming_events(request):
    """Get all upcoming events"""
    events = UpcomingEvents.objects.all()
    return [
        UpcomingEventsResponseSchema(
            id=event.pk,
            event_title=event.Eventtitle,
            event_topic=event.EventTopic,
            event_speaker_chairman=event.Eventspeaker_Chairman,
            event_date=event.Eventdate,
            event_time=event.Eventtime,
            event_venue=event.Eventvenue,
            flier=event.EventimageURL
        ) for event in events
    ]


@upcoming_events_router.get("/{event_id}", response=UpcomingEventsResponseSchema)
def get_upcoming_event(request, event_id: int):
    """Get a specific upcoming event by ID"""
    event = get_object_or_404(UpcomingEvents, id=event_id)
    return UpcomingEventsResponseSchema(
        id=event.pk,
        event_title=event.Eventtitle,
        event_topic=event.EventTopic,
        event_speaker_chairman=event.Eventspeaker_Chairman,
        event_date=event.Eventdate,
        event_time=event.Eventtime,
        event_venue=event.Eventvenue,
        flier=event.EventimageURL
    )


@upcoming_events_router.post("/", response=UpcomingEventsResponseSchema)
def create_upcoming_event(request, payload: UpcomingEventsCreateSchema):
    """Create a new upcoming event"""
    event = UpcomingEvents.objects.create(
        Eventtitle=payload.event_title,
        EventTopic=payload.event_topic,
        Eventspeaker_Chairman=payload.event_speaker_chairman,
        Eventdate=payload.event_date,
        Eventtime=payload.event_time,
        Eventvenue=payload.event_venue,
        Flier=payload.flier
    )
    
    return UpcomingEventsResponseSchema(
        id=event.pk,
        event_title=event.Eventtitle,
        event_topic=event.EventTopic,
        event_speaker_chairman=event.Eventspeaker_Chairman,
        event_date=event.Eventdate,
        event_time=event.Eventtime,
        event_venue=event.Eventvenue,
        flier=event.EventimageURL
    )


@upcoming_events_router.put("/{event_id}", response=UpcomingEventsResponseSchema)
def update_upcoming_event(request, event_id: int, payload: UpcomingEventsUpdateSchema):
    """Update an existing upcoming event"""
    event = get_object_or_404(UpcomingEvents, id=event_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'event_title': 'Eventtitle',
        'event_topic': 'EventTopic',
        'event_speaker_chairman': 'Eventspeaker_Chairman',
        'event_date': 'Eventdate',
        'event_time': 'Eventtime',
        'event_venue': 'Eventvenue',
        'flier': 'Flier'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(event, model_field, value)
    
    event.save()
    
    return UpcomingEventsResponseSchema(
        id=event.pk,
        event_title=event.Eventtitle,
        event_topic=event.EventTopic,
        event_speaker_chairman=event.Eventspeaker_Chairman,
        event_date=event.Eventdate,
        event_time=event.Eventtime,
        event_venue=event.Eventvenue,
        flier=event.EventimageURL
    )


@upcoming_events_router.delete("/{event_id}", response=UpcomingEventsDeleteSchema)
def delete_upcoming_event(request, event_id: int):
    """Delete an upcoming event"""
    event = get_object_or_404(UpcomingEvents, id=event_id)
    event.delete()
    return UpcomingEventsDeleteSchema(deleted_id=event_id)


# FAQ routes
@faq_router.get("/", response=List[FAQResponseSchema])
def list_faqs(request):
    """Get all FAQs"""
    faqs = FAQ.objects.all()
    return [
        FAQResponseSchema(
            id=faq.pk,
            question_number=faq.questionnumber,
            questions=faq.Questions,
            answer=faq.Answer
        ) for faq in faqs
    ]


@faq_router.get("/{faq_id}", response=FAQResponseSchema)
def get_faq(request, faq_id: int):
    """Get a specific FAQ by ID"""
    faq = get_object_or_404(FAQ, id=faq_id)
    return FAQResponseSchema(
        id=faq.pk,
        question_number=faq.questionnumber,
        questions=faq.Questions,
        answer=faq.Answer
    )


@faq_router.post("/", response=FAQResponseSchema)
def create_faq(request, payload: FAQCreateSchema):
    """Create a new FAQ"""
    faq = FAQ.objects.create(
        questionnumber=payload.question_number,
        Questions=payload.questions,
        Answer=payload.answer
    )
    
    return FAQResponseSchema(
        id=faq.pk,
        question_number=faq.questionnumber,
        questions=faq.Questions,
        answer=faq.Answer
    )


@faq_router.put("/{faq_id}", response=FAQResponseSchema)
def update_faq(request, faq_id: int, payload: FAQUpdateSchema):
    """Update an existing FAQ"""
    faq = get_object_or_404(FAQ, id=faq_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'question_number': 'questionnumber',
        'questions': 'Questions',
        'answer': 'Answer'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(faq, model_field, value)
    
    faq.save()
    
    return FAQResponseSchema(
        id=faq.pk,
        question_number=faq.questionnumber,
        questions=faq.Questions,
        answer=faq.Answer
    )


@faq_router.delete("/{faq_id}", response=FAQDeleteSchema)
def delete_faq(request, faq_id: int):
    """Delete a FAQ"""
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return FAQDeleteSchema(deleted_id=faq_id)


# Parents Review routes
@parents_review_router.get("/", response=List[ParentsReviewResponseSchema])
def list_parents_reviews(request):
    """Get all parents reviews"""
    reviews = ParentsReview.objects.all()
    return [
        ParentsReviewResponseSchema(
            id=review.pk,
            name=review.Name,
            occupation=review.Occupation,
            review=review.Review,
            profile_image=review.ParentsprofileimageURL
        ) for review in reviews
    ]


@parents_review_router.get("/{review_id}", response=ParentsReviewResponseSchema)
def get_parents_review(request, review_id: int):
    """Get a specific parents review by ID"""
    review = get_object_or_404(ParentsReview, id=review_id)
    return ParentsReviewResponseSchema(
        id=review.pk,
        name=review.Name,
        occupation=review.Occupation,
        review=review.Review,
        profile_image=review.ParentsprofileimageURL
    )


@parents_review_router.post("/", response=ParentsReviewResponseSchema)
def create_parents_review(request, payload: ParentsReviewCreateSchema):
    """Create a new parents review"""
    review = ParentsReview.objects.create(
        Name=payload.name,
        Occupation=payload.occupation,
        Review=payload.review,
        Profileimage=payload.profile_image
    )
    
    return ParentsReviewResponseSchema(
        id=review.pk,
        name=review.Name,
        occupation=review.Occupation,
        review=review.Review,
        profile_image=review.ParentsprofileimageURL
    )


@parents_review_router.put("/{review_id}", response=ParentsReviewResponseSchema)
def update_parents_review(request, review_id: int, payload: ParentsReviewUpdateSchema):
    """Update an existing parents review"""
    review = get_object_or_404(ParentsReview, id=review_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'name': 'Name',
        'occupation': 'Occupation',
        'review': 'Review',
        'profile_image': 'Profileimage'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(review, model_field, value)
    
    review.save()
    
    return ParentsReviewResponseSchema(
        id=review.pk,
        name=review.Name,
        occupation=review.Occupation,
        review=review.Review,
        profile_image=review.ParentsprofileimageURL
    )


@parents_review_router.delete("/{review_id}", response=ParentsReviewDeleteSchema)
def delete_parents_review(request, review_id: int):
    """Delete a parents review"""
    review = get_object_or_404(ParentsReview, id=review_id)
    review.delete()
    return ParentsReviewDeleteSchema(deleted_id=review_id)
