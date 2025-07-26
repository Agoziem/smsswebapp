from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import Subscription, Header, Contact
from ..schemas import (
    SubscriptionCreateSchema,
    SubscriptionUpdateSchema,
    SubscriptionResponseSchema,
    SubscriptionDeleteSchema,
    HeaderCreateSchema,
    HeaderUpdateSchema,
    HeaderResponseSchema,
    HeaderDeleteSchema,
    ContactCreateSchema,
    ContactUpdateSchema,
    ContactResponseSchema,
    ContactDeleteSchema
)

subscription_router = Router(tags=["Subscriptions"])
header_router = Router(tags=["Headers"])
contact_router = Router(tags=["Contacts"])


# Subscription routes
@subscription_router.get("/", response=List[SubscriptionResponseSchema])
def list_subscriptions(request):
    """Get all subscriptions"""
    subscriptions = Subscription.objects.all()
    return [SubscriptionResponseSchema.model_validate(sub) for sub in subscriptions]


@subscription_router.get("/{subscription_id}", response=SubscriptionResponseSchema)
def get_subscription(request, subscription_id: int):
    """Get a specific subscription by ID"""
    subscription = get_object_or_404(Subscription, id=subscription_id)
    return SubscriptionResponseSchema.model_validate(subscription)


@subscription_router.post("/", response=SubscriptionResponseSchema)
def create_subscription(request, payload: SubscriptionCreateSchema):
    """Create a new subscription"""
    subscription = Subscription.objects.create(Email=payload.email)
    return SubscriptionResponseSchema.model_validate(subscription)


@subscription_router.put("/{subscription_id}", response=SubscriptionResponseSchema)
def update_subscription(request, subscription_id: int, payload: SubscriptionUpdateSchema):
    """Update an existing subscription"""
    subscription = get_object_or_404(Subscription, id=subscription_id)
    
    update_data = payload.dict(exclude_unset=True)
    if 'email' in update_data:
        subscription.Email = update_data['email']
    
    subscription.save()
    return SubscriptionResponseSchema.model_validate(subscription)


@subscription_router.delete("/{subscription_id}", response=SubscriptionDeleteSchema)
def delete_subscription(request, subscription_id: int):
    """Delete a subscription"""
    subscription = get_object_or_404(Subscription, id=subscription_id)
    subscription.delete()
    return SubscriptionDeleteSchema(deleted_id=subscription_id)


# Header routes
@header_router.get("/", response=List[HeaderResponseSchema])
def list_headers(request):
    """Get all headers"""
    headers = Header.objects.all()
    return [
        HeaderResponseSchema(
            id=header.pk,
            about=header.About,
            aims_and_objectives=header.Aims_and_Objectives,
            vision=header.Vision,
            mission=header.Mission,
            snippet=header.snippet()
        ) for header in headers
    ]


@header_router.get("/{header_id}", response=HeaderResponseSchema)
def get_header(request, header_id: int):
    """Get a specific header by ID"""
    header = get_object_or_404(Header, id=header_id)
    return HeaderResponseSchema(
        id=header.pk,
        about=header.About,
        aims_and_objectives=header.Aims_and_Objectives,
        vision=header.Vision,
        mission=header.Mission,
        snippet=header.snippet()
    )


@header_router.post("/", response=HeaderResponseSchema)
def create_header(request, payload: HeaderCreateSchema):
    """Create a new header"""
    header = Header.objects.create(
        About=payload.about,
        Aims_and_Objectives=payload.aims_and_objectives,
        Vision=payload.vision,
        Mission=payload.mission
    )
    
    return HeaderResponseSchema(
        id=header.pk,
        about=header.About,
        aims_and_objectives=header.Aims_and_Objectives,
        vision=header.Vision,
        mission=header.Mission,
        snippet=header.snippet()
    )


@header_router.put("/{header_id}", response=HeaderResponseSchema)
def update_header(request, header_id: int, payload: HeaderUpdateSchema):
    """Update an existing header"""
    header = get_object_or_404(Header, id=header_id)
    
    update_data = payload.dict(exclude_unset=True)
    field_mapping = {
        'about': 'About',
        'aims_and_objectives': 'Aims_and_Objectives',
        'vision': 'Vision',
        'mission': 'Mission'
    }
    
    for key, value in update_data.items():
        model_field = field_mapping.get(key, key)
        setattr(header, model_field, value)
    
    header.save()
    
    return HeaderResponseSchema(
        id=header.pk,
        about=header.About,
        aims_and_objectives=header.Aims_and_Objectives,
        vision=header.Vision,
        mission=header.Mission,
        snippet=header.snippet()
    )


@header_router.delete("/{header_id}", response=HeaderDeleteSchema)
def delete_header(request, header_id: int):
    """Delete a header"""
    header = get_object_or_404(Header, id=header_id)
    header.delete()
    return HeaderDeleteSchema(deleted_id=header_id)


# Contact routes
@contact_router.get("/", response=List[ContactResponseSchema])
def list_contacts(request):
    """Get all contacts"""
    contacts = Contact.objects.all()
    return [ContactResponseSchema.model_validate(contact) for contact in contacts]


@contact_router.get("/{contact_id}", response=ContactResponseSchema)
def get_contact(request, contact_id: int):
    """Get a specific contact by ID"""
    contact = get_object_or_404(Contact, id=contact_id)
    return ContactResponseSchema.model_validate(contact)


@contact_router.post("/", response=ContactResponseSchema)
def create_contact(request, payload: ContactCreateSchema):
    """Create a new contact"""
    contact = Contact.objects.create(**payload.dict())
    return ContactResponseSchema.model_validate(contact)


@contact_router.put("/{contact_id}", response=ContactResponseSchema)
def update_contact(request, contact_id: int, payload: ContactUpdateSchema):
    """Update an existing contact"""
    contact = get_object_or_404(Contact, id=contact_id)
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(contact, key, value)
    
    contact.save()
    return ContactResponseSchema.model_validate(contact)


@contact_router.delete("/{contact_id}", response=ContactDeleteSchema)
def delete_contact(request, contact_id: int):
    """Delete a contact"""
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return ContactDeleteSchema(deleted_id=contact_id)
