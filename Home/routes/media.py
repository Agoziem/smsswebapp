from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import PhotoGallery, UpcomingEvents, ParentsReview
from ..schemas import (
    PhotoGalleryCreateSchema,
    PhotoGalleryUpdateSchema,
    PhotoGalleryResponseSchema,
    UpcomingEventsCreateSchema,
    UpcomingEventsUpdateSchema,
    UpcomingEventsResponseSchema,
    ParentsReviewCreateSchema,
    ParentsReviewUpdateSchema,
    ParentsReviewResponseSchema,
    SuccessResponseSchema
)

@api_controller("/photo-gallery", tags=["Photo Gallery"])
class PhotoGalleryController:

    @route.get("/", response=List[PhotoGalleryResponseSchema])
    def list_photos(self):
        """Get all photos in gallery"""
        return PhotoGallery.objects.all()

    @route.get("/{photo_id}", response=PhotoGalleryResponseSchema)
    def get_photo(self, photo_id: int):
        """Get a specific photo by ID"""
        return get_object_or_404(PhotoGallery, id=photo_id)

    @route.post("/", response=PhotoGalleryResponseSchema)
    def create_photo(self, payload: PhotoGalleryCreateSchema):
        """Create a new photo entry"""
        return PhotoGallery.objects.create(**payload.model_dump())

    @route.put("/{photo_id}", response=PhotoGalleryResponseSchema)
    def update_photo(self, photo_id: int, payload: PhotoGalleryUpdateSchema):
        """Update an existing photo entry"""
        photo = get_object_or_404(PhotoGallery, id=photo_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(photo, key, value)
        
        photo.save()
        return photo

    @route.delete("/{photo_id}", response={200: SuccessResponseSchema, 404: "Photo not found"})
    def delete_photo(self, photo_id: int):
        """Delete a photo entry"""
        photo = get_object_or_404(PhotoGallery, id=photo_id)
        photo.delete()
        return {"message": "Photo deleted successfully"}


@api_controller("/upcoming-events", tags=["Upcoming Events"])
class UpcomingEventsController:

    @route.get("/", response=List[UpcomingEventsResponseSchema])
    def list_events(self):
        """Get all upcoming events"""
        return UpcomingEvents.objects.all()

    @route.get("/{event_id}", response=UpcomingEventsResponseSchema)
    def get_event(self, event_id: int):
        """Get a specific event by ID"""
        return get_object_or_404(UpcomingEvents, id=event_id)

    @route.post("/", response=UpcomingEventsResponseSchema)
    def create_event(self, payload: UpcomingEventsCreateSchema):
        """Create a new upcoming event"""
        return UpcomingEvents.objects.create(**payload.model_dump())

    @route.put("/{event_id}", response=UpcomingEventsResponseSchema)
    def update_event(self, event_id: int, payload: UpcomingEventsUpdateSchema):
        """Update an existing event"""
        event = get_object_or_404(UpcomingEvents, id=event_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(event, key, value)
        
        event.save()
        return event

    @route.delete("/{event_id}", response={200: SuccessResponseSchema, 404: "Event not found"})
    def delete_event(self, event_id: int):
        """Delete an upcoming event"""
        event = get_object_or_404(UpcomingEvents, id=event_id)
        event.delete()
        return {"message": "Event deleted successfully"}


@api_controller("/parents-reviews", tags=["Parents Reviews"])
class ParentsReviewController:

    @route.get("/", response=List[ParentsReviewResponseSchema])
    def list_reviews(self):
        """Get all parents reviews"""
        return ParentsReview.objects.all()

    @route.get("/{review_id}", response=ParentsReviewResponseSchema)
    def get_review(self, review_id: int):
        """Get a specific review by ID"""
        return get_object_or_404(ParentsReview, id=review_id)

    @route.post("/", response=ParentsReviewResponseSchema)
    def create_review(self, payload: ParentsReviewCreateSchema):
        """Create a new parents review"""
        return ParentsReview.objects.create(**payload.model_dump())

    @route.put("/{review_id}", response=ParentsReviewResponseSchema)
    def update_review(self, review_id: int, payload: ParentsReviewUpdateSchema):
        """Update an existing review"""
        review = get_object_or_404(ParentsReview, id=review_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(review, key, value)
        
        review.save()
        return review

    @route.delete("/{review_id}", response={200: SuccessResponseSchema, 404: "Review not found"})
    def delete_review(self, review_id: int):
        """Delete a parents review"""
        review = get_object_or_404(ParentsReview, id=review_id)
        review.delete()
        return {"message": "Review deleted successfully"}
