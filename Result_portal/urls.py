from django.urls import path
from django.conf.urls import url
from .views import *
app_name = 'Result_portal'
urlpatterns = [
# Result Portal main Url
    path('', Result_Portal_view, name='classes'),
    path('<str:Classname>/<int:session_id>/', get_Students, name='get_students'),
      
]