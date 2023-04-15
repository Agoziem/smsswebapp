from django.db import models

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from .models import Student

# def login_view(request):
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         password = request.POST.get('password')

        # try:
        #     student = Student.objects.get(student_id=student_id)       
        # except Student.DoesNotExist:
        #     # Display an error message if the student does not exist
        #     messages.error(request, 'Student does not exist.')
        #     return render(request, 'login.html')
        
#         authenticated_student = authenticate(request, username=student_id, password=password)
#         if authenticated_student is not None:
#             # If the student exists, log them in and redirect to facilities page
#             login(request, student)
#             request.session['is_authenticated'] = True
#             return redirect('facilities')
#         else:
#             # If the student does not exist, create a new student and log them in
#             user = User.objects.create_user(username=student_id, password=password)
#             authenticated_student = authenticate(request, username=student_id, password=password)
#             login(request, authenticated_student)
#             request.session['is_authenticated'] = True
#             return redirect('facilities')
#         # Check if a student with the provided student_id and password exists
        
#     else:
#         return render(request, 'login.html')

