from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .groups import create_user_with_group
from Result_portal.models import Class
from Teachers_Portal.models import Teacher

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Teachers_portal:Teachers_dashboard')  # Replace 'home' with the name of your desired homepage URL
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def signup_view(request):
    classes = Class.objects.all()
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password2']
        Role = request.POST['Groupname']
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            email = ''
        if Role == 'Formteacher':
            classname = request.POST['Classname']
        try:
            User.objects.get(username=username)
            messages.error(request, 'Username is already taken.')
        except User.DoesNotExist:
            user = create_user_with_group(username, password, email, Role)
            login(request, user)
            if Role == 'Formteacher':
                class_formed=Class.objects.get(Class=classname)
                teacher = Teacher.objects.create(
                    user=user,
                    Role=Role,
                    classFormed=class_formed
                    )
                teacher.save()
            else:
                teacher = Teacher.objects.create(
                    user=user,
                    Role=Role,
                    )
                teacher.save()
            return redirect(reverse('Teachers_portal:profile', kwargs={'id': teacher.id }))  # Replace 'home' with the name of your desired homepage URL
    context = {
        'classes': classes
    }
    return render(request, 'sign_up.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('Teachers_portal:Teachers_dashboard')  # Replace 'home' with the name of your desired homepage URL
