from django.shortcuts import render,get_object_or_404,redirect
from Payment_portal.models import *
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from .models import * 

def initiate_payment(request):
	
	if request.method=='POST':

		name=request.POST.get('name')
		student_class=request.POST.get('class')
		payment_type=request.POST.get('type')
		term=request.POST.get('term')
		email=request.POST.get('email')
	
		amount_object=Amount.objects.get(description=payment_type)
		payment=Payment(Name_of_student=name,total_amount=amount_object.amount,Email=email)
		payment.save()
		payment.Payment_type.add(amount_object)
		payment.save()
		
		context={
			'payment': payment,
			'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
			"term":term
			}
		return render(request,'Make_payment2.html',context)
	
	else:
		payment_categories=Amount.objects.all()
		context={
			'payment_categories':payment_categories
			}
		return render(request,'Initiate_payment2.html',context)
		
def verify_payment(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	verified=payment.verify_payment()
	if verified:
		messages.success(request,"Your Payment was Successful")
		return render(request, 'Admission_form.html', { "receipt": payment })
	else:
		messages.error(request,"verification failed, check your inputs and try again") 
		return redirect('Initiate_payment2.html')
		

def admission_details(request,ref):
	payment=get_object_or_404(Payment,ref=ref)
	if request.method=='POST':
		FirstName=request.POST.get('FirstName')
		MiddleName=request.POST.get('MiddleName')
		LastName=request.POST.get('LastName')
		Address=request.POST.get('Address')
		Town=request.POST.get('Town')
		LGA=request.POST.get('LGA')
		gender=request.POST.get('Gender')
		State_of_Origin=request.POST.get('State_of_Origin')
		Nationality=request.POST.get('Nationality')
		School_attended=request.POST.get('School_attended')
		last_Class_passed=request.POST.get('last_Class_passed')
		Class_applying_for=request.POST.get('Class_applying_for')
		Disability=request.POST.get('Disability')
		Specify=request.POST.get('Specify')
		I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth=request.POST.get('I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth',"True")
		Parents_Name=request.POST.get('Parents_Name')
		Addressp=request.POST.get('Addressp')
		Phone_numberp=request.POST.get('Phone_numberp')
		Emailp=request.POST.get('Emailp')
		Religion=request.POST.get('religion')
		Church=request.POST.get('Church')
		Occupation=request.POST.get('Occupation')
		Comment=request.POST.get('Comment')
		
		student=NewStudent.objects.create(
			firstName=FirstName,
			MiddleName=MiddleName,
			lastName=LastName,
			address=Address,
			town=Town,
			lGA=LGA,
			gender=gender,
			state_of_Origin=State_of_Origin,
			nationality=Nationality,
			religion=Religion,
			school_attended=School_attended,
			Last_Class_passed=last_Class_passed,
			class_applying_for=Class_applying_for,
			disability=Disability,
			specify=Specify,
			certify=I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth,
			parents_Name=Parents_Name,
			addressp=Addressp,
			Emailp=Emailp,
			phone_numberp=Phone_numberp,
			Church=Church,
			Occupation=Occupation,
			Comment=Comment,
				)
		context={
			"payment":payment,
			"object":student,
		}
		messages.success(request,"Your Application was Successful Recorded")
		return render(request, 'Admission_details.html', context)
