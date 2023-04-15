from django.urls import path
from .views import *

app_name = 'Elibrary'
urlpatterns = [
    path('', category_view, name='subjects'),
    path('Ebooklist/',ebooklist_view, name='ebooklist'),
    path('<int:id>/detail/',ebookdetail_view, name='ebookdetail'),
    path('download-book/', download_book, name='download_book'),
    
    ]