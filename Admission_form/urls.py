from django.urls import path
from .views import *

app_name = 'Admission_form'
urlpatterns = [
	path('',initiate_payment, name='initiate_payment'),
	path('details/', admission_details , name='details'),
	path('<str:ref>/',verify_payment, name='verify_payment'),
    ]