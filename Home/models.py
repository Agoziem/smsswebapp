from django.db import models
from ckeditor.fields import RichTextField
from Result_portal.models import Class
import random
import secrets

class School(models.Model):
	Schoolid=models.IntegerField()
	Schoollogo=models.ImageField(upload_to='assets/Schoollogo', blank=True)
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
	
	def managementimageURL(self):
		try:
			url= self.Profileimage.url
		except:
			url=""
		return url

class Teacher(models.Model):
	Name= models.CharField(max_length= 200, blank=True)
	Phone_number= models.CharField(max_length= 200, blank=True)
	Email= models.EmailField(max_length= 200, blank=True)
	Role= models.CharField(max_length= 200, blank=True , default="Teacher")
	Subject=models.CharField(max_length= 200, blank=False, help_text="if more than one , add it comma-separated")
	Classes_assigned=models.ManyToManyField(Class)
	teachers_id=models.CharField(max_length= 200, blank=True)
	teachers_password=models.CharField(max_length= 200, blank=True)
	Headshot=models.ImageField(upload_to='assets/TeachersProfileimages', blank=True)
	
	
	def __str__(self):
		return str(self.Name)

	@property
	def profileimageURL(self):
		try:
			url= self.Headshot.url
		except:
			url=""
		return url
	
	def save(self, *args, **kwargs):
		if self.id:  # if object exists in database
			super().save(*args, **kwargs)  # simply update the fields
		else:  # if object is new
			while not self.teachers_id:
				random_pin = str(random.randint(1000, 9999))
				random_password = secrets.token_urlsafe(8)
				Application_id = f"teacher/smss/{random_pin}"
				object_with_similar_Application_id = Teacher.objects.filter(teachers_id=random_pin, teachers_password=random_password)
				if not object_with_similar_Application_id:
					self.teachers_id = Application_id
					self.teachers_password = random_password
			super().save(*args, **kwargs)
	
class FormTeachers(models.Model):
	Form_teachers_Name= models.CharField(max_length= 200, blank=True)
	Class=models.OneToOneField(Class, on_delete=models.CASCADE, blank=True, null=True )
	Form_teachers_Headshot=models.ImageField(upload_to='assets/TeachersProfileimages', blank=True)
	Form_teachers_id=models.CharField(max_length= 200, blank=True)
	Form_teachers_password=models.CharField(max_length= 200, blank=True)
	

	def __str__(self):
		return str(self.Form_teachers_Name)
	
	@property
	def Formteachersimage(self):
		try:
			url= self.Form_teachers_Headshot.url
		except:
			url=""
		return url
	
	def save(self, *args, **kwargs):
		if self.id:  # if object exists in database
			super().save(*args, **kwargs)  # simply update the fields
		else:  # if object is new
			while not self.Form_teachers_id:
				random_pin = str(random.randint(1000, 9999))
				random_password = secrets.token_urlsafe(8)
				Application_id = f"formteacher/smss/{random_pin}"
				object_with_similar_Application_id = FormTeachers.objects.filter(Form_teachers_id=random_pin, Form_teachers_password=random_password)
				if not object_with_similar_Application_id:
					self.Form_teachers_id = Application_id
					self.Form_teachers_password = random_password
			super().save(*args, **kwargs)


				
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
	Photo=models.ImageField(upload_to='assets/photogallery')
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


# s3 = boto3.client("s3")
# bucket_name= "smssbucket"
# s3_object="media/assets/No image.svg"
# obj=s3.get_object(Bucket=bucket_name,Key=s3_object)
class UpcomingEvents(models.Model):
	Flier=models.ImageField(upload_to='assets/eventfliers', blank=True)
	Eventtitle= models.CharField(max_length= 300, blank=True)
	EventTopic= models.CharField(max_length= 300, blank=True)
	Eventspeaker_Chairman= models.CharField(max_length= 300, blank=True)
	Eventdate= models.CharField(max_length= 300, blank=True)
	Eventtime= models.CharField(max_length= 300, blank=True)
	Eventvenue= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Eventtitle)
	
	@property
	def EventimageURL(self):
		try:
			url= self.Flier.url
		except:
			url=""
		return url
		
class FAQ(models.Model):
	questionnumber=models.CharField(max_length= 300, blank=True,help_text="use alphabets like one , two & three")
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

class ParentsReview(models.Model):
	Profileimage=models.ImageField(upload_to='assets/parentsProfileimages', blank=True )
	Name=models.CharField(max_length= 300, blank=True)
	Occupation= models.CharField(max_length= 300, blank=True)
	Review= models.TextField(blank=True)
	
	def __str__(self):
		return str(self.Name)
	
	@property
	def ParentsprofileimageURL(self):
		try:
			url= self.Profileimage.url
		except:
			url=""
		return url