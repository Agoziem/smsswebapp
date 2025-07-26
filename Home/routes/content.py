from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import Subscription, Header, Contact, FAQ
from ..schemas import (
    SubscriptionCreateSchema,
    SubscriptionUpdateSchema,
    SubscriptionResponseSchema,
    HeaderCreateSchema,
    HeaderUpdateSchema,
    HeaderResponseSchema,
    ContactCreateSchema,
    ContactUpdateSchema,
    ContactResponseSchema,
    FAQCreateSchema,
    FAQUpdateSchema,
    FAQResponseSchema,
    SuccessResponseSchema
)

@api_controller("/subscriptions", tags=["Subscriptions"])
class SubscriptionController:

    @route.get("/", response=List[SubscriptionResponseSchema])
    def list_subscriptions(self):
        """Get all subscriptions"""
        return Subscription.objects.all()

    @route.get("/{subscription_id}", response=SubscriptionResponseSchema)
    def get_subscription(self, subscription_id: int):
        """Get a specific subscription by ID"""
        return get_object_or_404(Subscription, id=subscription_id)

    @route.post("/", response=SubscriptionResponseSchema)
    def create_subscription(self, payload: SubscriptionCreateSchema):
        """Create a new subscription"""
        return Subscription.objects.create(**payload.model_dump())

    @route.put("/{subscription_id}", response=SubscriptionResponseSchema)
    def update_subscription(self, subscription_id: int, payload: SubscriptionUpdateSchema):
        """Update an existing subscription"""
        subscription = get_object_or_404(Subscription, id=subscription_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(subscription, key, value)
        
        subscription.save()
        return subscription

    @route.delete("/{subscription_id}", response={200: SuccessResponseSchema, 404: "Subscription not found"})
    def delete_subscription(self, subscription_id: int):
        """Delete a subscription"""
        subscription = get_object_or_404(Subscription, id=subscription_id)
        subscription.delete()
        return {"message": "Subscription deleted successfully"}


@api_controller("/headers", tags=["Headers"])
class HeaderController:

    @route.get("/", response=List[HeaderResponseSchema])
    def list_headers(self):
        """Get all headers"""
        return Header.objects.all()

    @route.get("/{header_id}", response=HeaderResponseSchema)
    def get_header(self, header_id: int):
        """Get a specific header by ID"""
        return get_object_or_404(Header, id=header_id)

    @route.post("/", response=HeaderResponseSchema)
    def create_header(self, payload: HeaderCreateSchema):
        """Create a new header"""
        return Header.objects.create(**payload.model_dump())

    @route.put("/{header_id}", response=HeaderResponseSchema)
    def update_header(self, header_id: int, payload: HeaderUpdateSchema):
        """Update an existing header"""
        header = get_object_or_404(Header, id=header_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(header, key, value)
        
        header.save()
        return header

    @route.delete("/{header_id}", response={200: SuccessResponseSchema, 404: "Header not found"})
    def delete_header(self, header_id: int):
        """Delete a header"""
        header = get_object_or_404(Header, id=header_id)
        header.delete()
        return {"message": "Header deleted successfully"}


@api_controller("/contacts", tags=["Contacts"])
class ContactController:

    @route.get("/", response=List[ContactResponseSchema])
    def list_contacts(self):
        """Get all contacts"""
        return Contact.objects.all()

    @route.get("/{contact_id}", response=ContactResponseSchema)
    def get_contact(self, contact_id: int):
        """Get a specific contact by ID"""
        return get_object_or_404(Contact, id=contact_id)

    @route.post("/", response=ContactResponseSchema)
    def create_contact(self, payload: ContactCreateSchema):
        """Create a new contact"""
        return Contact.objects.create(**payload.model_dump())

    @route.put("/{contact_id}", response=ContactResponseSchema)
    def update_contact(self, contact_id: int, payload: ContactUpdateSchema):
        """Update an existing contact"""
        contact = get_object_or_404(Contact, id=contact_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(contact, key, value)
        
        contact.save()
        return contact

    @route.delete("/{contact_id}", response={200: SuccessResponseSchema, 404: "Contact not found"})
    def delete_contact(self, contact_id: int):
        """Delete a contact"""
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return {"message": "Contact deleted successfully"}


@api_controller("/faqs", tags=["FAQs"])
class FAQController:

    @route.get("/", response=List[FAQResponseSchema])
    def list_faqs(self):
        """Get all FAQs"""
        return FAQ.objects.all()

    @route.get("/{faq_id}", response=FAQResponseSchema)
    def get_faq(self, faq_id: int):
        """Get a specific FAQ by ID"""
        return get_object_or_404(FAQ, id=faq_id)

    @route.post("/", response=FAQResponseSchema)
    def create_faq(self, payload: FAQCreateSchema):
        """Create a new FAQ"""
        return FAQ.objects.create(**payload.model_dump())

    @route.put("/{faq_id}", response=FAQResponseSchema)
    def update_faq(self, faq_id: int, payload: FAQUpdateSchema):
        """Update an existing FAQ"""
        faq = get_object_or_404(FAQ, id=faq_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(faq, key, value)
        
        faq.save()
        return faq

    @route.delete("/{faq_id}", response={200: SuccessResponseSchema, 404: "FAQ not found"})
    def delete_faq(self, faq_id: int):
        """Delete a FAQ"""
        faq = get_object_or_404(FAQ, id=faq_id)
        faq.delete()
        return {"message": "FAQ deleted successfully"}
