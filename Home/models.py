from django.db import models
from ckeditor.fields import RichTextField

class School(models.Model):
	Schoolid=models.IntegerField()
	Schoollogo=models.ImageField(upload_to='assets', blank=True)
	Schoolname= models.CharField(max_length= 300, blank=True)
	SchoolPhonenumber= models.CharField(max_length= 300, blank=True)
	Schoolmotto= models.CharField(max_length= 300, blank=True)
	Schoollocation= models.CharField(max_length= 300, blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterpage= models.CharField(max_length= 300, blank=True)
	Whatsapp= models.CharField(max_length= 300, blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Schoolname)
		
	@property
	def imageURL(self):
		try:
			url= self.Schoollogo.url
		except:
			url=''
		return url
		
class Management(models.Model):
	Profileimage=models.ImageField(upload_to='assets', blank=True)
	Profilename= models.CharField(max_length= 300, blank=True)
	Role= models.CharField(max_length= 300, blank=True)
	Phonenumber= models.CharField(max_length= 300, blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterpage= models.CharField(max_length= 300, blank=True)
	Whatsapp= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Profilename)
		
class Subscription(models.Model):
	Email= models.EmailField(blank = True,null=True)
	
	def __str__(self):
		return str(self.Email)
		
class Header(models.Model):
	About=RichTextField(blank=True,null=True)
	Aims_and_Objectives= RichTextField(blank=True,null=True)
	Vision=models.TextField(blank=True,null=True)
	Mission=models.TextField(blank=True,null=True)
	
	def snippet(self):
		return self.About[:220] + '...'

class PhotoGallery(models.Model):
	Photo=models.ImageField(upload_to='assets')
	Description= models.CharField(max_length= 300, blank=False)
	
	def __str__(self):
		return str(self.Description)

	@property
	def imageURL(self):
		try:
			url= self.Photo.url
		except:
			url=''
		return url
		
class UpcomingEvents(models.Model):
	Flier=models.ImageField(upload_to='assets', blank=True)
	Eventtitle= models.CharField(max_length= 300, blank=True)
	EventTopic= models.CharField(max_length= 300, blank=True)
	Eventspeaker_Chairman= models.CharField(max_length= 300, blank=True)
	Eventdate= models.CharField(max_length= 300, blank=True)
	Eventtime= models.CharField(max_length= 300, blank=True)
	Eventvenue= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Eventtitle)
		
class FAQ(models.Model):
	questionnumber=models.CharField(max_length= 300, blank=True)
	Questions= models.CharField(max_length= 300, blank=True)
	Answer= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Questions)

class Contact(models.Model):
	name = models.CharField(max_length=100)
	message = models.CharField(max_length=80)
	email = models.EmailField()

	def __str__(self):
		return str(self.email)
