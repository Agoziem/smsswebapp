from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from Result_portal.models import Class
from Home.models import School
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

def initiate_payment(request):
    if request.method=='POST':

        # collect the Vlaues from the Form
        name=request.POST.get('name')
        student_class=request.POST.get('class')
        payment_type=request.POST.get('type')
        term=request.POST.get('term')
        email=request.POST.get('email')

        # Query the database tables with it
        Class_object=Class.objects.get(Class=student_class)
        amount_object=Amount.objects.get(description=payment_type)
        payment=Payment(Name_of_student=name,student_class=Class_object,Payment_type=amount_object,Email=email)
        payment.save()
        print(amount_object)
        context={
        'payment': payment,
        'paymentamount': amount_object,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
        "term":term
        }
        return render(request,'Make_payment.html',context)
        
    else:
        Class_list=Class.objects.all()
        payment_categories=Amount.objects.all()
        context={
            'Class_list':Class_list,
            'payment_categories':payment_categories
        }
        return render(request,'Initiate_payment.html',context)
		
def verify_payment(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	amount=get_object_or_404(Amount,description=payment.Payment_type)
	verified=payment.verify_payment()
	if verified:
		messages.success(request,"payment successful")
		return render(request, 'Online_receipt.html', { "receipt": payment , "paidamount": amount })
	else:
		messages.error(request,"verification failed, check your inputs and try again") 
		return redirect('Initiate_payment.html')
		

