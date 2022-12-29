from django.shortcuts import render,redirect
from .models import PhotoGallery,School,Management,Subscription,Header,FAQ,UpcomingEvents,Contact
# from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import json



def home_view(request):
	context= {
	}
	return render(request,'404.html',context)

def home2_view(request):
	queryset1=School.objects.all()
	queryset2=Management.objects.all()
	queryset3=Header.objects.all()
	queryset4=FAQ.objects.all()
	queryset5=UpcomingEvents.objects.all()
	queryset6=PhotoGallery.objects.all()
	
	photos=[]
	homePhotos=[]
	for photoobject in queryset6:
		photos.append(photoobject)
		homePhotos=photos[:6]
	context= {
	'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'schools':queryset1,
	'managements':queryset2,
	'headers':queryset3,
	'FAQ':queryset4,
	'events':queryset5,
	'photos':homePhotos,
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
