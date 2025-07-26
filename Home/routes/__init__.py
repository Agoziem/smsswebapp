from .schools import router as schools_router
from .staff import management_router, top_teacher_router
from .content import subscription_router, header_router, contact_router
from .media import photo_gallery_router, upcoming_events_router, faq_router, parents_review_router

__all__ = [
    "schools_router",
    "management_router", 
    "top_teacher_router",
    "subscription_router", 
    "header_router", 
    "contact_router",
    "photo_gallery_router", 
    "upcoming_events_router", 
    "faq_router", 
    "parents_review_router"
]
