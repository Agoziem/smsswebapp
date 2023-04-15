from django.urls import path
from .views import *

app_name = 'Attendance'
urlpatterns = [
	path('',attendance_view , name='class_attendance'),
	path('mark_attendance/',mark_attendance, name='mark_attendance'),
    path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    ]