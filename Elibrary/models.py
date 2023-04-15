from django.db import models

class Subject(models.Model):
	Sub= models.CharField(max_length= 200, blank=True)
	Icon=models.ImageField(upload_to='assets', blank=True)
	
	def __str__(self):
		return str(self.Sub)

	@property
	def iconURL(self):
		try:
			url= self.Icon.url
		except:
			url=''
		return url
	
class Ebook(models.Model):
	Ebookcategory= models.ForeignKey(Subject, related_name='Subject' , on_delete=models.CASCADE , blank = True,null=True)
	Ebookimage=models.CharField(max_length= 300, blank=True)
	EbookTitle= models.CharField(max_length= 300, blank=True)
	Ebookdescription= models.CharField(max_length= 400, blank=True)
	Ebookauthor= models.CharField(max_length= 300, blank=True)
	Ebooklink= models.CharField(max_length= 300, blank=True)
	date_uploaded=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.EbookTitle)



    # other fields go here

class Download(models.Model):
    book = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

