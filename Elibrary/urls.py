from django.urls import path
from .views import *

app_name = 'Elibrary'
urlpatterns = [
    path('', category_view, name='subjects'),
    path('<int:cate>/',ebooklist_view, name='ebooklist'),
    path('<int:id>/detail/',ebookdetail_view, name='ebookdetail'),
    
    ]