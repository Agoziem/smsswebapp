from django.shortcuts import render,redirect
from .models import *
from Teachers_Portal.models import Teacher
from Result_portal.models import *
from Blog.models import Article
# from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import json



def activation_view(request):
	print(request.path)
	context={
	}
	return render(request, "activation.html" ,context)

# //////////////////////////////////////////////////////////
# Upload Excel files
def upload(request):
    if request.method == 'POST' and request.FILES.get('myFile'):
        myfile = request.FILES['myFile']
        instance = Excelfiles(Excel=myfile)
        instance.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})
    
def createPin(request):
	student=Excelfiles()
	student.readPin()
	context = {
		}
	return render(request, "pins.html", context)

def home_view(request):
	queryset1=School.objects.all()
	queryset2=Management.objects.all()
	queryset3=Header.objects.all()
	queryset4=FAQ.objects.all()
	queryset5=UpcomingEvents.objects.order_by('-id')[:2]
	queryset6=PhotoGallery.objects.order_by('-id')[:6]
	queryset7=Teacher.objects.all()
	queryset8=ParentsReview.objects.all()
	queryset9=Article.objects.order_by('-id')[:4]
	context= {
	'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'schools':queryset1,
	'managements':queryset2,
	'headers':queryset3,
	'FAQ':queryset4,
	'events':queryset5,
	'photos':queryset6,
	"Teachers":queryset7,
	"parentsreviews":queryset8,
	"articles":queryset9
	}
	return render(request,'home.html',context)
	
def about_view(request):
	queryset3=Header.objects.all()
	context= {
	'headers':queryset3,
	}
	return render(request,'about.html',context)

def photo_gallery_view(request):
	Photos=PhotoGallery.objects.all().order_by('-id',)
	context= {
	"photos":Photos,
	}
	return render(request,'photogallery.html',context)
	
# def home2_view(request):
# 	if request.method == 'POST':
# 		emails=request.POST.get('email')
# 		"""
# 		subject = "Welcome message"
# 		message = "thanks for subscribing to our newsletter, you start receiving our newsletter"
# 		sender=settings.EMAIL_HOST_USER
# 		recipients = [emails]
# 		send_mail(subject, message, sender, recipients, fail_silently=False)
# 		"""
# 		Subscription.objects.create(Email=emails)
# 		messages.success(request, 'thanks for subscribing, you will start receiving our newsletters')
# 		return redirect('home')

def submit_contact_form(request):
    data=json.loads(request.body)
    contactname=data['userformdata']['name']
    contactemail=data['userformdata']['email']
    contactmessage=data['userformdata']['message']
    contact_info=Contact.objects.create(
        name=contactname,
        email=contactemail,
        message=contactmessage
    )
    contact_info.save()

    return JsonResponse('submitted successfully',safe=False)

def submit_sub_form(request):
    data=json.loads(request.body)
    subemail=data['userdata']['email']
    sub_email=Subscription.objects.create(Email=subemail)
    sub_email.save()
    return JsonResponse('submitted successfully',safe=False)
