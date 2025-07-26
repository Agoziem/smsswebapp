from typing import Optional
from ninja import Field, ModelSchema, Schema
from django.contrib.auth.models import User

class UserResponseSchema(ModelSchema):
    """Schema for user response"""
    class Meta:
        model = User
        fields = '__all__'


class UserMinimalSchema(Schema):
    """Minimal user schema for responses"""
    id: int = Field(..., description="User ID")
    username: str = Field(..., max_length=150, description="Username")
    email: Optional[str] = Field(None, description="User email address")