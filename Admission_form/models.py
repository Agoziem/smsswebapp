from django.db import models
from Payment_portal.models import Amount
from Payment_portal.Paystack import Paystack
import random
import secrets


boolChoice = (
		("Yes","Yes"),("No","No")
		)
GenderChoice = (
		("Male","Male"),("Female","Female")
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
	gender=models.CharField(max_length=100, choices=GenderChoice, blank=True)
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
	Occupation=models.CharField(max_length=100, blank=True)
	Comment=models.CharField(max_length=100,blank=True)
	Admitted=models.BooleanField(default=False,blank=True)
	application_id=models.CharField(max_length=100, blank=True)
	Password=models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f"{self.firstName} {self.lastName}"


	def save(self,*args,**kwargs):
		while not self.application_id:
			random_pin=str(random.randint(1000, 9999))
			random_password=secrets.token_urlsafe(8)
			Application_id = f"app/smss/{random_pin}"
			object_with_similar_Application_id=NewStudent.objects.filter(application_id=random_pin,Password=random_password)
			if not object_with_similar_Application_id:
				self.application_id=Application_id
				self.Password=random_password
			super().save(*args,**kwargs)
