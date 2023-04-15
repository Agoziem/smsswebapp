from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# def teacher_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_teacher:
#             login(request, user)
#             return redirect('teacher_dashboard')
#         else:
#             error_message = "Invalid username or password."
#             return render(request, 'teacher_login.html', {'error_message': error_message})
#     else:
#         return render(request, 'teacher_login.html')
