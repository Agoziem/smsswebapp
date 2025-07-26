from typing import Optional
from ninja import ModelSchema, Schema, Field

from Accounts.schemas import UserMinimalSchema
from Blog.models import Article


class ArticleResponseSchema(ModelSchema):
    author: UserMinimalSchema = Field(..., description="Author of the article")

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSchema(Schema):
    """Schema for creating a new article"""
    author_id: Optional[int] = Field(None, description="Author user ID")
    title: str = Field(..., max_length=100, description="Article title")
    slug: Optional[str] = Field(None, description="Article slug")
    body: str = Field(..., description="Article content")
    thumb: Optional[str] = Field(None, description="Article thumbnail image")

class ArticleUpdateSchema(Schema):
    """Schema for updating an article"""
    title: Optional[str] = Field(None, max_length=100, description="Article title")
    slug: Optional[str] = Field(None, description="Article slug")
    body: Optional[str] = Field(None, description="Article content")
    thumb: Optional[str] = Field(None, description="Article thumbnail image")


class ErrorResponseSchema(Schema):
    error: str


class SuccessResponseSchema(Schema):
    message: str
