from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ArticleBase(BaseModel):
    title: str = Field(..., max_length=100, description="Article title")
    slug: Optional[str] = Field(None, description="Article slug")
    body: str = Field(..., description="Article content")
    thumb: Optional[str] = Field(None, description="Article thumbnail image")


class ArticleCreateSchema(ArticleBase):
    """Schema for creating a new article"""
    author_id: Optional[int] = Field(None, description="Author user ID")


class ArticleUpdateSchema(BaseModel):
    """Schema for updating an article"""
    title: Optional[str] = Field(None, max_length=100, description="Article title")
    slug: Optional[str] = Field(None, description="Article slug")
    body: Optional[str] = Field(None, description="Article content")
    thumb: Optional[str] = Field(None, description="Article thumbnail image")
    author_id: Optional[int] = Field(None, description="Author user ID")


class ArticleResponseSchema(ArticleBase):
    """Schema for article response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    date: datetime
    author_id: Optional[int] = Field(None, description="Author user ID")
    author_username: Optional[str] = Field(None, description="Author username")
    snippet: Optional[str] = Field(None, description="Article snippet")


class ArticleDeleteSchema(BaseModel):
    """Schema for article deletion confirmation"""
    message: str = Field(default="Article deleted successfully")
    deleted_id: int
