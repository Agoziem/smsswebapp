from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from Result_portal.models import Class
from Home.models import School
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

def initiate_payment(request):
    if request.method=='POST':
    # collect the values from the form
        name = request.POST.get('name')
        student_class = request.POST.get('class')
        
        payment_type_ids = [int(payment_id) for payment_id in request.POST.get('item_ids[]').split(',')]
        term = request.POST.get('term')
        email = request.POST.get('email')

        # Query the database tables with it
        class_object = Class.objects.get(Class=student_class)
        payment = Payment(Name_of_student=name, student_class=class_object, total_amount=0, Email=email)
        payment.save()

        for payment_type_id in payment_type_ids:
            payment_type = Amount.objects.get(id=payment_type_id)
            payment.Payment_type.add(payment_type)
            payment.total_amount += payment_type.amount
        payment.save()

        context = {
            'payment': payment,
            'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
            'term': term
        }
        return render(request, 'Make_payment.html', context)  
    else:
        Class_list=Class.objects.all()
        payment_category=Amount.objects.all()
        context={
            'Class_list':Class_list,
            'payment_category':payment_category
        }
        return render(request,'Initiate_payment.html',context)
		
def verify_payment(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	verified=payment.verify_payment()
	if verified:
		messages.success(request,"payment successful")
		return render(request, 'Online_receipt.html', { "receipt": payment  })
	else:
		messages.error(request,"verification failed, check your inputs and try again") 
		return redirect('Initiate_payment.html')
		

