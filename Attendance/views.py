from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from Result_portal.models import Students_Pin_and_ID,Class
from .models import Attendance
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.db import transaction
from Home.models import FormTeachers



# the main Attandance Home page 
def attendance_view(request):
    classes = Class.objects.all()
    context={
        'classes': classes,
        }
    return render(request, 'teacher_login.html', context)

# login view
def mark_attendance(request):
    classes = Class.objects.all()
    if request.method == 'POST':
        classname=request.POST['class_name']
        form_teachers_id = request.POST['form_teachers_id']
        form_teachers_password = request.POST['form_teachers_password']
        try:
            attendance_class=get_object_or_404(Class, Class=classname)
            form_teacher = FormTeachers.objects.get(Form_teachers_id=form_teachers_id, Form_teachers_password=form_teachers_password,Class=attendance_class.id)
            students = Students_Pin_and_ID.objects.filter(student_class=classname)
            context={
                "form_teacher":form_teacher,
                "students":students,
                "attendance_class":attendance_class,
            }
			# If form teacher exists, redirect to success page
            return render(request, 'mark_attendance.html', context)
        except FormTeachers.DoesNotExist:
			# If form teacher does not exist, display error message
            error_message = 'Check your input and try again'
            context={
                "classes":classes,
                "error_message":error_message,
            }
            return render(request, 'teacher_login.html',context)
    else:
        context={
        'classes': classes,
        }
        return render(request, 'teacher_login.html', context)

        



def post_attendance(request,classname):
    if request.method == 'POST':
        date = request.POST.get('date')
        present_students = request.POST.getlist('present_students')
        formteacherid=request.POST.get('teacher_id')
        teacher = FormTeachers.objects.get(id=formteacherid)
        attendance_class=get_object_or_404(Class, Class=classname)
        try:
            with transaction.atomic():
                # Hard delete records older than a week
                Attendance.objects.filter(
                    Q(date__lte=timezone.now()-timedelta(weeks=1)) |
                    Q(deleted_at__lte=timezone.now()-timedelta(weeks=1))
                ).delete()
                # Add new records

                for student_id in present_students:
                    student = get_object_or_404(Students_Pin_and_ID, id=student_id, student_class=classname)
                    attendance = Attendance(date=date, is_present=True, student=student, form_teacher=teacher)
                    attendance.save()
                context={
                    "attendance_class":attendance_class,
                }
                messages.success(request, "Attendance marked successfully")
                return render(request, 'congratulations.html',context)
        except IntegrityError:
            messages.error(request, "Attendance already marked for one or more students")
            return redirect('/', classname=attendance_class.Class)





