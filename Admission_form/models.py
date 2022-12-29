from django.db import models
from Payment_portal.models import Amount
from Payment_portal.Paystack import Paystack


boolChoice = (
		("Yes","Yes"),("No","No")
		)

class NewStudent(models.Model):
	firstName=models.CharField(max_length=100, blank=True)
	MiddleName=models.CharField(max_length=100, blank=True)
	lastName=models.CharField(max_length=100, blank=True)
	address=models.CharField(max_length=100, blank=True)
	town=models.CharField(max_length=100, blank=True)
	lGA=models.CharField(max_length=100, blank=True)
	state_of_Origin=models.CharField(max_length=100, blank=True)
	nationality=models.CharField(max_length=100, blank=True)
	gender=models.CharField(max_length=100, blank=True)
	school_attended=models.CharField(max_length=100, blank=True)
	Last_Class_passed=models.CharField(max_length=100, blank=True)
	class_applying_for=models.CharField(max_length=100, blank=True)
	disability=models.CharField(max_length=100, choices=boolChoice, blank=True) 
	specify=models.CharField(max_length=200, blank=True,null=True)
	certify=models.BooleanField(default=False,blank=True)
	parents_Name=models.CharField(max_length=100, blank=True)
	addressp=models.CharField(max_length=100, blank=True)
	phone_numberp=models.CharField(max_length=100, blank=True)
	Emailp=models.CharField(max_length=100, blank=True)
	religion=models.CharField(max_length=100, blank=True)
	Church=models.CharField(max_length=100, blank=True)
	Comment=models.CharField(max_length=100, choices=boolChoice, blank=True)
	Admitted=models.BooleanField(default=False,blank=True)
	
