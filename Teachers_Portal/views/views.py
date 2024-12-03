from django.shortcuts import render, redirect
from Result_portal.models import *
from ..models import *
from ..forms import TeacherForm
from django.contrib.auth.decorators import login_required
from CBT.models import *
from django.db.models import Q


# Teachers Dashbord View
@login_required
def Teachers_dashboard_view(request):
    sessions = AcademicSession.objects.all()
    context={
        "sessions":sessions
    }
    return render(request,'Teachers_dashboard.html',context)

# Teachers profile View
@login_required
def profile_view(request, id):
    teacher = Teacher.objects.get(id=id)
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    sessions = AcademicSession.objects.all()

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        role = request.POST.get("Role")
        class_formed = request.POST.get("classFormed")

        if form.is_valid():
            teacher = form.save(commit=False)

            # Update the Role
            teacher.Role = role

            # Only assign classFormed if Role is 'Form-teacher'
            if role == "Formteacher":
                if class_formed:
                    teacher.classFormed_id = class_formed
            else:
                teacher.classFormed = None  # Reset if Role is not Form-teacher
            teacher.save()
            form.save_m2m()  # Save ManyToMany fields
            return redirect('Teachers_portal:Teachers_dashboard')

    context = {
        'teacher': teacher,
        'classes': classes,
        'subjects': subjects,
        'form': TeacherForm(instance=teacher),
        'sessions': sessions,
    }
    return render(request, 'teachers/editprofile.html', context)







