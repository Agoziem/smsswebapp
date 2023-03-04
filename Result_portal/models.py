from django.db import models
from openpyxl import Workbook,load_workbook
import boto3
import io
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from openpyxl.utils import get_column_letter
import os
import random
from ckeditor.fields import RichTextField


# Model for the Classes
		
class Class(models.Model):
	Class=models.CharField(max_length=10, blank=True)
	
	def __str__(self):
		return str(self.Class)

# Model for the Newsletter Section & Assignments

class Newsletter(models.Model):
	newsletter= RichTextField(blank=True,null=True)

class Assignments(models.Model):
	Class= models.ForeignKey(Class, related_name='classes' , on_delete=models.CASCADE , blank = True,null=True)
	subject=models.CharField(max_length=200, blank=True)
	file=models.FileField(upload_to = 'media' ,blank = True)

	def __str__(self):
		return str(self.subject)


# Model for Annual Result

class AnnualResult(models.Model):
	SN= models.CharField(max_length=100, blank=True ,null=True , default="-")
	Name=models.CharField(max_length=200, blank=True,null=True,default="No name")
	Class=models.CharField(max_length=100, blank=True,null=True ,default="No class")
	Subject= models.CharField(max_length=100, blank=True,null=True,default="-")
	FirstTerm= models.CharField(max_length=100, blank=True,null=True,default="-")
	SecondTerm= models.CharField(max_length=100, blank=True,null=True,default="-")
	ThirdTerm= models.CharField(max_length=100, blank=True,null=True,default="-")
	Total= models.CharField(max_length=100, blank=True,null=True,default="-")
	Average= models.CharField(max_length=100, blank=True,null=True,default="-")
	Grade=models.CharField(max_length=100, blank=True,null=True,default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True,null=True,default="-")
	Remark=models.CharField(max_length= 100, blank=True,null=True, default="-")

	def __str__(self):
		return str(self.Name +"-"+ self.Subject+"-"+self.Class)

#Models for Annual Students Details

class AnnualStudent(models.Model):
	Name=models.CharField(max_length=200, blank=True,null=True , default="No name")
	Class=models.CharField(max_length=100, blank=True,null=True , default="No class")
	TotalScore=models.CharField(max_length=100, blank=True,null=True , default="-")
	Totalnumber=models.CharField(max_length=100, blank=True,null=True , default="-")
	Average=models.CharField(max_length=100, blank=True,null=True , default="-")
	Position=models.CharField(max_length=100, blank=True,null=True , default="-")
	Term=models.CharField(max_length=100, blank=True,null=True , default="-")
	Academicsession=models.CharField(max_length=100, blank=True,null=True , default="-")

	def __str__(self):
		return str(self.Name+"-"+self.Class)

# //////////////////////////////////////////////////////////////////////////////////

# Functions for Annual Students Result ACtivation

# Jss1A //
	def createJuniorAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)						
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)					
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)		
# Jss 2 //
	def createJuniorAnnual2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
				
					elif count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
# Jss 3 //
	def createJuniorAnnual3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)					
# SS1
	def createSeniorAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1CAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,29),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					elif count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 14:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 15:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 16:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 17:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					elif count == 18:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					elif count == 19:
						for count, col in enumerate(range(1,15),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)	
# SS2
	def createSeniorAnnual2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2BAnnual.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,24),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 13:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 14:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# SS3///
	def createSeniorAnnual3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3BAnnual.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,24),start=1):
					if count == 1:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 2:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 3:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 4:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 5:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 6:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 7:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 8:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 9:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					if count == 10:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 11:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 12:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value

					if count == 13:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					
					if count == 14:
						for count, col in enumerate(range(1,11),start=1):
							char=get_column_letter(col)
								
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								FirstTerm=ws[char+str(row)].value
							elif count == 4:
								SecondTerm=ws[char+str(row)].value
							elif count == 5:
								ThirdTerm=ws[char+str(row)].value
							elif count == 6:
								Total=ws[char+str(row)].value
							elif count == 7:
								Average=ws[char+str(row)].value
							elif count == 8:
								Grade=ws[char+str(row)].value
							elif count == 9:
								SubjectPosition=ws[char+str(row)].value
							elif count == 10:
								Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

# /////////////////////////////////////////////////////////////////////////


# Model for Termly Result

class Result(models.Model):
	SN= models.CharField(max_length=100, blank=True,null=True , default="-")
	Name=models.CharField(max_length=200, blank=True,null=True , default="No name")
	Class=models.CharField(max_length=100, blank=True,null=True , default="No class")
	Subject= models.CharField(max_length=100, blank=True,null=True , default="-")
	FirstTest= models.CharField(max_length=100, blank=True,null=True , default="-")
	FirstAss= models.CharField(max_length=100, blank=True,null=True , default="-")
	Project= models.CharField(max_length=100, blank=True,null=True , default="-")
	SecondAss= models.CharField(max_length=100, blank=True,null=True , default="-")
	SecondTest= models.CharField(max_length=100, blank=True,null=True , default="-")
	CA= models.CharField(max_length=100, blank=True,null=True , default="-")
	Exam= models.CharField(max_length=100, blank=True,null=True , default="-")
	Total= models.CharField(max_length=100, blank=True,null=True , default="-")
	Grade=models.CharField(max_length=100, blank=True,null=True , default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True,null=True , default="-")
	Remark=models.CharField(max_length= 100, blank=True,null=True , default="-")
	
	
					
	def __str__(self):
		return str(self.Name +"-"+ self.Subject+"-"+self.Class)


# Model for the Termly Students data

class Student(models.Model):
	Name=models.CharField(max_length=200, blank=True,null=True , default="No name")
	Class=models.CharField(max_length=100, blank=True,null=True , default="No class")
	TotalScore=models.CharField(max_length=100, blank=True,null=True , default="-")
	Totalnumber=models.CharField(max_length=100, blank=True,null=True , default="-")
	Average=models.CharField(max_length=100, blank=True,null=True , default="-")
	Position=models.CharField(max_length=100, blank=True,null=True , default="-")
	Term=models.CharField(max_length=100, blank=True,null=True , default="-")
	Academicsession=models.CharField(max_length=100, blank=True,null=True , default="-")
	
	
	
	def __str__(self):
		return str(self.Name+"-"+self.Class)

# ////////////////////////////////////////////////////////////////////

# Termly Students Result

# Jss1 //
	def createJuniorResult1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)# Jss2 //

# Jss2 //
	def createJuniorResult2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
	
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)# Jss2 //
# Jss3 ///
	def createJuniorResult3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,23),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
	
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)# Jss2 //
# Ss1 //
	def createSeniorResult1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1CTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,30),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value

					elif count == 14:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 15:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 16:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 17:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					elif count == 18:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value

					elif count == 19:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					elif count == 20:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)					

# SS2 //
	def createSeniorResult2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2BTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,24),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					
					if count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value

					if count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value

					if count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 14:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)					
# SS3 //
	def createSeniorResult3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3BTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				for count, row in enumerate(range(10,24),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value				
					if count == 2:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 3:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 4:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 5:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 6:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 7:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 8:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 9:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 10:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 11:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 12:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 13:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)
							
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					if count == 14:
						for count, col in enumerate(range(1,14),start=1):
							char=get_column_letter(col)		
							if count == 1:
								SN=ws[char+str(row)].value
							elif count == 2:
								Subject=ws[char+str(row)].value
							elif count == 3:
								ResTest=ws[char+str(row)].value
							elif count == 4:
								FirstAss=ws[char+str(row)].value
							elif count == 5:
								Project=ws[char+str(row)].value
							elif count == 6:
								SecondAss=ws[char+str(row)].value
							elif count == 7:
								SecondTest=ws[char+str(row)].value
							elif count == 8:
								CA=ws[char+str(row)].value
							elif count == 9:
								Exam=ws[char+str(row)].value
							elif count == 10:
								Total=ws[char+str(row)].value
							elif count == 11:
								Grade=ws[char+str(row)].value
							elif count == 12:
								SubjectPosition=ws[char+str(row)].value
							elif count == 13:
								Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=ResTest,SecondTest=SecondTest,Project=Project,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)					
		



# Model for the Excel Files 

class Excelfiles(models.Model):
	Excel= models.FileField(upload_to ='media' ,blank = True)
	
	def __str__(self):
		return str(self.Excel)


# /////////////////////////////////////////////////////////////

	# Termly Students Data

# Jss1 ///
	def createJuniorStudent1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss2 /// 
	def createJuniorStudent2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss3 //
	def createJuniorStudent3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3CTermly.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3DTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# SS1 //
	def createSeniorStudents1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1BTermly.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1CTermly.xlsx')
		seniorClassExcel=[obj,obj2,obj3]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K30'].value
				Average=ws['H30'].value
				TotalScore=ws['E30'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# SS2 ///
	def createSeniorStudents2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2BTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# SS3 // 
	def createSeniorStudents3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3ATermly.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3BTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)			


# /////////////////////////////////////////////////////////////////
# Annual Students Data 

	def createJuniorStudentAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss1DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['P25'].value
				Average=ws['M25'].value
				TotalScore=ws['J25'].value
				Totalnumber=ws['k6'].value
				Term=ws['M6'].value
				Academicsession=ws['P6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss2 //
	def createJuniorStudentAnnual2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss2DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss3 //
	def createJuniorStudentAnnual3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3CAnnual.xlsx')
		obj4= s3.get_object(Bucket='smsswebbucket', Key='media/media/Jss3DAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3,obj4]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss1 //
	def createSeniorStudentsAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1BAnnual.xlsx')
		obj3= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS1CAnnual.xlsx')
		seniorClassExcel=[obj,obj2,obj3]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K29'].value
				Average=ws['H29'].value
				TotalScore=ws['E29'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss2 //
	def createSeniorStudentsAnnual2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS2BAnnual.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss3 //
	def createSeniorStudentsAnnual3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3AAnnual.xlsx')
		obj2= s3.get_object(Bucket='smsswebbucket', Key='media/media/SS3BAnnual.xlsx')
		seniorClassExcel=[obj,obj2]
		for file in seniorClassExcel:
			binary_data = file['Body'].read()
			wb = load_workbook(io.BytesIO(binary_data))
			for sheet in wb:
				ws=wb[sheet.title]
				Name=str(ws['B4'].value).upper().strip()
				Class=ws['B6'].value
				Position=ws['K25'].value
				Average=ws['H25'].value
				TotalScore=ws['E25'].value
				Totalnumber=ws['F6'].value
				Term=ws['H6'].value
				Academicsession=ws['K6'].value
				AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)




# Create Students 

	def readPin(self,*args,**kwargs)-> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='smsswebbucket', Key='media/media/Students_details_Main_SMSS.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data),data_only=True)
		for sheet in wb:
			ws=wb[sheet.title]
			for count, row in enumerate(range(6,56),start=1):
				if count == 1:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 2:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 3:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 4:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 5:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 6:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 7:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 8:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 9:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 10:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 11:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 12:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 13:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 14:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 15:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 16:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 17:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 18:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 19:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 20:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 21:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 22:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 23:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 24:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 25:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 26:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 27:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 28:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 29:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 30:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 31:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 32:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 33:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 34:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 35:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 36:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 37:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 38:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 39:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 40:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 41:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 42:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 43:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 44:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 45:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 46:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 47:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 48:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 49:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				if count == 50:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=str(ws[char+str(row)].value).upper().strip()
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
				Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)   
# Model for the Pins		

class Students_Pin_and_ID(models.Model):
	SN=models.CharField(max_length=100, blank=True,null=True)
	student_name=models.CharField(max_length=100, blank=True, default="No name",null=True)
	student_id=models.CharField(max_length=100, blank=True,null=True)
	student_pin= models.CharField(max_length=100, blank=True,null=True)
	student_class=models.CharField(max_length=100, blank=True,null=True,default="No class")

	def __str__(self):
		return str(self.student_name)

	   
   
   
    # def generatePin(self,*args,**kwargs):
    #     i=0
    #     while i <= 300:
    #         StudentPin= str(random.randint(0, 99999999999999)).rjust(14, '0')
    #         pin=StudentPin
    #         Pin.objects.create(pin=pin)
    #         i=i+1
    # def __str__(self):
    #     return str(self.student)
        
# Read it back to Excel

    # def save(self,*args,**kwargs):
    #     Name = str(self.student).upper().strip()
    #     self.student=Name
    #     super().save(*args,**kwargs)
		