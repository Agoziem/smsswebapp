from django.urls import path
from .views import *

app_name = 'CBT'
urlpatterns = [
    path('',CBT_view, name='CBT_center'),
    path('<str:Classname>/', get_Students, name='get_students'),
	path('Teachers_login/',Teachers_cbt_authentication , name='authentication'),
    path('add_questionset/',add_questionset , name='add_questionset'),
    ]