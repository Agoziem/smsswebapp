from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from Result_portal.models import Students_Pin_and_ID
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


def category_view(request):
	queryset= Subject.objects.all()
	context = {
		"subjects": queryset,
    }
	return render(request, "Subjects.html", context)

def ebooklist_view(request):
	subjects= Subject.objects.all()
	if request.method=='POST':
		student_id=str(request.POST.get('student_id'))
		Password=str(request.POST.get('student_password'))
		student_cate=int(request.POST.get('Subject_Category'))

		try:
			student = Students_Pin_and_ID.objects.get(student_id=student_id,student_password=Password)
			queryset=Ebook.objects.filter(Ebookcategory=student_cate)
			queryset2=Subject.objects.get(id=student_cate)
			context = {
				"categories":subjects,
				"ebooks": queryset,
				"ebooksubject":queryset2,
				"student":student,
			}
			return render(request, "Ebooks.html", context)
		except Students_Pin_and_ID.DoesNotExist:
			# Display an error message if the student does not exist
			context = {
				"subjects": subjects,
			}
			messages.error(request, 'Check the Student id or the Pin and try again')
			return render(request, "Subjects.html", context)

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




def download_book(request):
    data=json.loads(request.body)
    book_id=data['book_id']
    print(book_id)
    book = Ebook.objects.get(id=book_id)
    Download.objects.create(book=book)
    download_count = Download.objects.filter(book=book).count()
    return JsonResponse({'status': 'ok','download_count': download_count},safe=False)