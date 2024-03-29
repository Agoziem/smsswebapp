from django.db import models
import secrets
from Result_portal.models import Class
from .Paystack import Paystack

class Amount(models.Model):
	amount=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
	description=models.CharField(max_length=100, blank=True)
	
	def __str__(self):
		return str(self.description)
		
	

	
class Payment(models.Model):
	Name_of_student=models.CharField(max_length=100, blank=True)
	student_class=models.ForeignKey(Class, related_name='Level', on_delete=models.CASCADE, blank=True, null=True )
	Payment_type=models.ManyToManyField(Amount, related_name='payments' )
	ref=models.CharField(max_length=100, blank=False)
	Email =models.EmailField()
	verified=models.BooleanField(default=False)
	date_created=models.DateTimeField(auto_now_add=True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	
	class Meta:
		ordering = ('-date_created',)
	
	@property
	def amount_value(self) -> int:
		return self.total_amount*100
	
	def save(self,*args,**kwargs):
		while not self.ref:
			ref = secrets.token_urlsafe(20)
			object_with_similar_ref=Payment.objects.filter(ref=ref)
			if not object_with_similar_ref:
				self.ref=ref
			super().save(*args,**kwargs)
			
	
	def __str__(self):
		return str(self.Name_of_student)
	
	def verify_payment(self):
		paystack= Paystack()
		status = paystack.verify_payment(self.ref)
		if status:
			self.verified = True
			super().save()
		if self.verified:
			return True
		return False

