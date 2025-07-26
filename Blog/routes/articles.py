from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from typing import List

from ninja_extra import api_controller, route

from ..models import Article
from ..schemas import (
    ArticleCreateSchema,
    ArticleUpdateSchema,
    ArticleResponseSchema,
)

@api_controller("/articles", tags=["Articles"])
class ArticleController:

    @route.get("/", response=List[ArticleResponseSchema])
    def list_articles(self):
        """Get all articles"""
        articles = Article.objects.select_related('author').all()
        return articles


    @route.get("/{article_id}", response=ArticleResponseSchema)
    def get_article(self, article_id: int):
        """Get a specific article by ID"""
        article = get_object_or_404(Article, id=article_id)
        return article


    @route.post("/", response=ArticleResponseSchema)
    def create_article(self, payload: ArticleCreateSchema):
        """Create a new article"""
        article_data = payload.dict(exclude_unset=True)
        
        # Handle author assignment
        if 'author_id' in article_data:
            author = get_object_or_404(User, id=article_data.pop('author_id'))
            article_data['author'] = author
        
        article = Article.objects.create(**article_data)
        
        return article


    @route.put("/{article_id}", response=ArticleResponseSchema)
    def update_article(self, article_id: int, payload: ArticleUpdateSchema):
        """Update an existing article"""
        article = get_object_or_404(Article, id=article_id)
        
        update_data = payload.dict(exclude_unset=True)
        
        # Handle author update
        if 'author_id' in update_data:
            author = get_object_or_404(User, id=update_data.pop('author_id'))
            update_data['author'] = author
        
        for key, value in update_data.items():
            setattr(article, key, value)
        
        article.save()
        
        return article


    @route.delete("/{article_id}", response={200: "Article deleted successfully", 404: "Article not found"})
    def delete_article(self, article_id: int):
        """Delete an article"""
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return {"message": "Article deleted successfully"}
