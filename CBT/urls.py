from django.urls import path
from .views import *

app_name = 'CBT'
urlpatterns = [
	path('',Teachers_cbt_authentication , name='authentication'),
    path('add_questionset/',add_questionset , name='add_questionset'),
	# path('mark_attendance/',mark_attendance, name='mark_attendance'),
    # path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    ]