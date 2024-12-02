from django.shortcuts import render
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from CBT.models import *


# for Class Attendance
@login_required
def attendance_view(request,Classname):
    sessions = AcademicSession.objects.all()
    classobject = Class.objects.all()
    context={
        'class':classobject,
        "sessions":sessions
    }
    return render(request, 'formteachers/attendance.html', context)

# Post Class Attendance
def post_attendance(request,classname):
    context={

    }
    return JsonResponse(context)





