from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from typing import List

from ..models import Article
from ..schemas import (
    ArticleCreateSchema,
    ArticleUpdateSchema,
    ArticleResponseSchema,
    ArticleDeleteSchema
)

router = Router(tags=["Articles"])


@router.get("/", response=List[ArticleResponseSchema])
def list_articles(request):
    """Get all articles"""
    articles = Article.objects.select_related('author').all()
    return [
        ArticleResponseSchema(
            id=article.pk,
            title=article.title,
            slug=article.slug,
            body=article.body,
            thumb=article.thumb.url if article.thumb else None,
            date=article.date,
            author_id=article.author.pk if article.author else None,
            author_username=article.author.username if article.author else None,
            snippet=article.snippet()
        ) for article in articles
    ]


@router.get("/{article_id}", response=ArticleResponseSchema)
def get_article(request, article_id: int):
    """Get a specific article by ID"""
    article = get_object_or_404(Article, id=article_id)
    return ArticleResponseSchema(
        id=article.pk,
        title=article.title,
        slug=article.slug,
        body=article.body,
        thumb=article.thumb.url if article.thumb else None,
        date=article.date,
        author_id=article.author.pk if article.author else None,
        author_username=article.author.username if article.author else None,
        snippet=article.snippet()
    )


@router.post("/", response=ArticleResponseSchema)
def create_article(request, payload: ArticleCreateSchema):
    """Create a new article"""
    article_data = payload.dict(exclude_unset=True)
    
    # Handle author assignment
    if 'author_id' in article_data:
        author = get_object_or_404(User, id=article_data.pop('author_id'))
        article_data['author'] = author
    
    article = Article.objects.create(**article_data)
    
    return ArticleResponseSchema(
        id=article.pk,
        title=article.title,
        slug=article.slug,
        body=article.body,
        thumb=article.thumb.url if article.thumb else None,
        date=article.date,
        author_id=article.author.pk if article.author else None,
        author_username=article.author.username if article.author else None,
        snippet=article.snippet()
    )


@router.put("/{article_id}", response=ArticleResponseSchema)
def update_article(request, article_id: int, payload: ArticleUpdateSchema):
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
    
    return ArticleResponseSchema(
        id=article.pk,
        title=article.title,
        slug=article.slug,
        body=article.body,
        thumb=article.thumb.url if article.thumb else None,
        date=article.date,
        author_id=article.author.pk if article.author else None,
        author_username=article.author.username if article.author else None,
        snippet=article.snippet()
    )


@router.delete("/{article_id}", response=ArticleDeleteSchema)
def delete_article(request, article_id: int):
    """Delete an article"""
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return ArticleDeleteSchema(deleted_id=article_id)
