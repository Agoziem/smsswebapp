from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.decorators import login_required

def category_view(request):
	queryset= Subject.objects.all()
	context = {
		"subjects": queryset,
    }
	return render(request, "Subjects.html", context)

def ebooklist_view(request,cate):
	queryset=Ebook.objects.filter(Ebookcategory=cate)
	queryset2=Subject.objects.get(id=cate)
	queryset3= Subject.objects.all()
	context = {
		"ebooks": queryset,
		"ebooksubject":queryset2,
		'categories' : queryset3,
    }
	return render(request, "Ebooks.html", context)

def ebookdetail_view(request,id):
	stuff=get_object_or_404(Ebook,id=id)
	#total_shares= stuff.shares()
	#total_downloads= stuff.downloads()
	#total_views= stuff.views()
	context={
		"object":stuff,
		#"total_shares":total_shares,
		#"total_downloads":total_downloads,
		#"total_views":total_views,
		}
	return render(request,"Ebookdetail.html", context)
	