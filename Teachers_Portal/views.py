from django.shortcuts import render, redirect, get_object_or_404
from Result_portal.models import *
from .models import *
from django.http import JsonResponse
from .forms import TeacherForm
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json
from django.db.models import Q


# Teachers Dashbord View
@login_required
def Teachers_dashboard_view(request):
    context={

    }
    return render(request,'Teachers_dashboard.html',context)

# Teachers profile View
@login_required
def profile_view(request,id):
    teacher = Teacher.objects.get(id=id)
    classes=Class.objects.all()
    subjects=Subject.objects.all()
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save() 
            return redirect('Teachers_portal:Teachers_dashboard')
    
    context={
        'teacher': teacher,
        'classes':classes,
        'subjects':subjects,
        'form':form
    }
    return render(request,'editprofile.html',context)


# Teachers Result Formulation Part
@login_required
def result_computation_view(request,Classname):
    classobject = Class.objects.get(Class=Classname)
    context={
        'class':classobject,
        } 
    return render(request,'Result_computation.html',context)

@login_required
def get_students_result_view(request, Classname, subject):
    classobject = Class.objects.get(Class=Classname)
    subjectobject = Subject.objects.get(subject_name=subject)
    students = Students_Pin_and_ID.objects.filter(student_class=classobject)
    studentResults = []
    
    for studentresult in students:
        # Assuming student_result_data is a related name in your Students_Pin_and_ID model
        student_result_object, created = Result.objects.get_or_create(student=studentresult,Subject=subjectobject,student_class=classobject)
        studentResults.append({
            'student_name': f'<a class="editstudentinfo text-decoration-none" style="cursor:pointer">{student_result_object.student.student_name}</a>',
            'FT': student_result_object.FirstTest,
            'FA': student_result_object.FirstAss,
            'MTT': student_result_object.MidTermTest,
            'SA': student_result_object.SecondAss,
            'ST': student_result_object.SecondTest,
            'CA': student_result_object.CA,
            'Exam': student_result_object.Exam,
            'Total': student_result_object.Total,
            'Grade': student_result_object.Grade,
            # 'Position': student_result_object.SubjectPosition,
            'Remark': student_result_object.Remark,
        })

    return JsonResponse(studentResults, safe=False)

@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    subject=data['subject']
    Classdata=data['student_class']
    student=data['studentname']
    classobject= Class.objects.get(Class=Classdata)
    studentobject= Students_Pin_and_ID.objects.get(student_name=student)
    subjectobject = Subject.objects.get(subject_name=subject)
    studentResult = Result.objects.get(student=studentobject,Subject=subjectobject,student_class=classobject)
    studentResult.FirstTest  = int(data['FirstTest'])  
    studentResult.FirstAss  = int(data['FirstAss'])
    studentResult.MidTermTest = int(data['MidTermTest'])
    studentResult.SecondAss = int(data['SecondAss'])
    studentResult.SecondTest = int(data['SecondTest'])
    studentResult.Exam = int(data['Exam'])
    studentResult.save()

    studentResults = []
    student_result_object = Result.objects.filter(Subject=subjectobject,student_class=classobject)
    for student_result_object in student_result_object:
        student_result_object.refresh_from_db()
        studentResults.append({
            'student_name': f'<a class="editstudentinfo text-decoration-none" style="cursor:pointer">{student_result_object.student.student_name}</a>',
            'FT': student_result_object.FirstTest,
            'FA': student_result_object.FirstAss,
            'MTT': student_result_object.MidTermTest,
            'SA': student_result_object.SecondAss,
            'ST': student_result_object.SecondTest,
            'CA': student_result_object.CA,
            'Exam': student_result_object.Exam,
            'Total': student_result_object.Total,
            'Grade': student_result_object.Grade,
            # 'Position': student_result_object.SubjectPosition,
            'Remark': student_result_object.Remark,
        })

    return JsonResponse(studentResults, safe=False)
    







# CBT Teachers Views for CRUD and Submitting Questions
@login_required
def CBT_Questions_view(request,teachers_id):
    subjects=Subject.objects.all()
    classes=Class.objects.all()
    teacher=Teacher.objects.get(id=teachers_id)

    if request.method == 'POST':
        classname = request.POST.getlist('test_classes')  # Assuming classname is a list
        subject = Subject.objects.get(id=request.POST['subject'])
        time = request.POST['testTime']

        query = Q(subject=subject)
        for class_name in classname:
            query &= Q(ExamClass__id__icontains=class_name)

        if QuestionSet.objects.filter(query).exists():
            questionset = QuestionSet.objects.filter(query).order_by('-id').first()
        else:
            questionset = QuestionSet.objects.create(
                subject=subject,
                examTime=time,
                teacher=teacher
            )
            for class_id in classname:
                class_object = Class.objects.get(id=class_id)
                questionset.ExamClass.add(class_object)
            questionset.save()

        context = {'questionSet': questionset}
        return render(request, 'CBT_Questions.html', context)

    context={
        "subjects":subjects,
        "classes":classes,
        "teacher":teacher
    }
    return render(request,'CBT_details.html',context)

def CBT_update_details(request,id):
    questionset = QuestionSet.objects.get(id=id)
    if request.method == 'POST':
        classname=request.POST.getlist('test_classes')
        time=request.POST['testTime']
        questionset.examTime = time
        questionset.ExamClass.clear()
        class_objects = Class.objects.filter(id__in=classname)
        questionset.ExamClass.add(*class_objects)
        questionset.save()
        context={
            'questionSet':questionset
        }
        return render(request,'CBT_Questions.html',context)
    context={
        "questionset":questionset
    }
    return render(request,'CBT_update_details.html',context)

def submitquestion_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject_name = data.get('subject')
        teacher_name = data.get('teacher')
        exam_time = data.get('examTime')
        classes = data.get('Class')

        # Get or create Subject and Teacher instances
        subject = Subject.objects.get(subject_name=subject_name)
        teacher = Teacher.objects.get(FirstName=teacher_name)
            
        query = Q(subject=subject)
        for class_name in classes:
            query &= Q(ExamClass__Class__icontains=class_name)

        if QuestionSet.objects.filter(query).exists():
            question_set = QuestionSet.objects.get(query)

        else:
            question_set = QuestionSet.objects.create(
                examTime=exam_time,
                teacher=teacher,
                subject=subject
            )

        # Process the list of questions
        questions_data = data['questions']
        for question_data in questions_data:
            question_id = question_data.get('id') # this is the questionid
            required = question_data.get('questionrequired')
            
            # get the Question and set its required property
            question = Question.objects.get(
                questionId =question_id,
            )
            question.required=required
            question.save()

            # get the nswers and set its is_correct property
            answers_data = question_data['answers']
            for answer_data in answers_data:
                answer_id = answer_data.get('id')
                is_correct = answer_data.get('isCorrect')

                answer = Answer.objects.get(
                    answerId=answer_id,
                )
                answer.isCorrect=is_correct
                answer.save()
                question.answers.add(answer)

            question_set.questions.add(question)

        # Add the selected classes to the QuestionSet
        for class_name in classes:
            class_obj, created = Class.objects.get_or_create(Class=class_name)
            question_set.ExamClass.add(class_obj)

        return JsonResponse({'message': 'Questions and answers submitted successfully'})  # Return a success response

    return JsonResponse({'error': 'Invalid request method'})

@login_required
def CBT_result_view(request):
    context={

    }
    return render(request,'CBT_results.html',context)

# ////////////////////////////

# Form teachers View for CRUD Students Details
@login_required
def Students_view(request,Classname):
    classobject = Class.objects.get(Class=Classname)
    students = Students_Pin_and_ID.objects.filter(student_class=classobject)
    context={
        'class':classobject,
        "students":students
        } 
    return render(request,'students.html',context)

def createstudent_view(request):
    data=json.loads(request.body)
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    classobject = Class.objects.get(Class=student_class)
    try:
        newStudent = Students_Pin_and_ID.objects.create(student_name=student_name,Sex=student_sex,student_class=classobject)
        newStudentResult = Student_Result_Data.objects.create(Student_name=newStudent)
        context={
            'student_ID': newStudent.id, 
            'student_id': newStudent.student_id, 
            'student_name':newStudent.student_name,
            'student_sex':newStudent.Sex,
            'message': f'{newStudent.student_name} record have been created Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)
    
def updatestudent_view(request):
    data=json.loads(request.body)
    student_id=data['studentID']
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    classobject = Class.objects.get(Class=student_class)
    try:
        updateStudent = Students_Pin_and_ID.objects.get(id=student_id)
        updateStudent.student_name=student_name
        updateStudent.Sex= student_sex
        updateStudent.student_class=classobject
        updateStudent.save()
        context={
            'student_ID': updateStudent.id, 
            'student_id': updateStudent.student_id, 
            'student_name':updateStudent.student_name,
            'student_sex':updateStudent.Sex,
            'message': f'{updateStudent.student_name} record have been updated Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)

def DeleteStudents_view(request):
    studentidstodelete=json.loads(request.body)
    studentnamesdeleted=[]   
    try:
        for id in studentidstodelete:
            student = Students_Pin_and_ID.objects.get(id=id)
            studentnamesdeleted.append(student.student_name)
            student.delete()
        context={
            'message': f'{studentnamesdeleted} records have been deleted Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)


# for Class Attendance
@login_required
def attendance_view(request,Classname):
    classobject = Class.objects.all()
    context={
        'class':classobject
    }
    return render(request, 'attendance.html', context)

# Post Class Attendance
def post_attendance(request,classname):
    context={

    }
    return JsonResponse(context)





