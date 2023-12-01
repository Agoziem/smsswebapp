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
def result_computation_view(request,Classname,id):
    teacher = Teacher.objects.get(id=id)
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    classobject = Class.objects.get(Class=Classname)
    subjectsforclass=Subjectallocation.objects.get(classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))

    context={
            'class':classobject,
            "Terms":Terms,
            "academic_session":academic_session,
            "subjects_taught_for_class":subjects_taught_for_class
        }
    return render(request,'Result_computation.html',context)

@login_required
def get_students_result_view(request):
    data=json.loads(request.body)
    classobject = Class.objects.get(Class=data['studentclass'])
    subjectobject = Subject.objects.get(subject_name=data['studentsubject'])
    term=Term.objects.get(term=data['selectedTerm'])
    session=AcademicSession.objects.get(session=data['selectedAcademicSession'])
    students = Students_Pin_and_ID.objects.filter(student_class=classobject)
    studentResults = []
    
    for studentresult in students:
        student_result_details,created = Student_Result_Data.objects.get_or_create(Student_name=studentresult,Term=term,AcademicSession=session)
        student_result_object, created = Result.objects.get_or_create(student=studentresult, Subject=subjectobject, students_result_summary=student_result_details,student_class=classobject)
        try:
            total_test_score = TestQuestionSet.objects.get(
                testSubject=subjectobject, testSetGroup__student=studentresult
            )
            student_result_object.MidTermTest = total_test_score.testTotalScore
        except:
            student_result_object.MidTermTest = student_result_object.MidTermTest
        studentResults.append({
            'Name': student_result_object.student.student_name,
            '1sttest': student_result_object.FirstTest,
            '1stAss': student_result_object.FirstAss,
            'MidTermTest': student_result_object.MidTermTest,
            '2ndTest': student_result_object.SecondAss,
            '2ndAss': student_result_object.SecondTest,
            'Exam': student_result_object.Exam,
        })

    return JsonResponse(studentResults, safe=False)

@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['studentsubject']
    Classdata=data['classdata']['studentclass']
    student=data['formDataObject']['Name']
    classobject= Class.objects.get(Class=Classdata)
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    studentobject= Students_Pin_and_ID.objects.get(student_name=student)
    subjectobject = Subject.objects.get(subject_name=subject)
    student_result_details = Student_Result_Data.objects.get(Student_name=studentobject,Term=term,AcademicSession=session)
    studentResult = Result.objects.get(student=studentobject,students_result_summary=student_result_details, Subject=subjectobject,student_class=classobject)
    studentResult.FirstTest  = data['formDataObject']['1sttest']
    studentResult.FirstAss  = data['formDataObject']['1stAss']
    studentResult.MidTermTest  = data['formDataObject']['MidTermTest']
    studentResult.SecondAss = data['formDataObject']['2ndAss']
    studentResult.SecondTest = data['formDataObject']['2ndTest']
    studentResult.Exam = data['formDataObject']['Exam']
    studentResult.save()

    return JsonResponse('Result Updated Successfully', safe=False)
    

def submitallstudentresult_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['studentsubject']
    Classdata=data['classdata']['studentclass']
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    for result in data['data']:
        classobject= Class.objects.get(Class=Classdata)
        subjectobject = Subject.objects.get(subject_name=subject)
        studentobject= Students_Pin_and_ID.objects.get(student_name=result['Name'])
        student_result_details = Student_Result_Data.objects.get(Student_name=studentobject,Term=term,AcademicSession=session)
        studentResult = Result.objects.get(student=studentobject,students_result_summary=student_result_details, Subject=subjectobject,student_class=classobject)
        studentResult.FirstTest=result['1sttest']
        studentResult.FirstAss=result['1stAss']
        studentResult.MidTermTest=result['MidTermTest']
        studentResult.SecondAss=result['2ndTest']
        studentResult.SecondTest=result['2ndAss']
        studentResult.CA=result['CA']
        studentResult.Exam=result['Exam']
        studentResult.Total=result['Total']
        studentResult.Grade=result['Grade']
        studentResult.SubjectPosition=result['Position']
        studentResult.Remark=result['Remarks']
        studentResult.save()
    return JsonResponse('Results submitted Successfully', safe=False)





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
        query &= Q(ExamClass__id__in=classname)

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
        teacher = Teacher.objects.filter(FirstName=teacher_name).first()
        query = Q(subject=subject)
        query &= Q(ExamClass__id__in=classes)

        if QuestionSet.objects.filter(query).exists():
            question_set = QuestionSet.objects.filter(query).order_by('-id').first()
        else:
            question_set = QuestionSet.objects.create(
                examTime=exam_time,
                teacher=teacher,
                subject=subject
            )
            for class_name in classes:
                class_obj, created = Class.objects.get_or_create(Class=class_name)
                question_set.ExamClass.add(class_obj)
            question_set.save()
        questions_data = data['questions']
        for question_data in questions_data:
            question_id = question_data.get('id')
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

        return JsonResponse({'message': 'Questions and answers submitted successfully'})  # Return a success response

    return JsonResponse({'error': 'Invalid request method'})


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




# Form teachers View for submitting Results
@login_required
def PublishResults_view(request,Classname):
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list':subject_code,
        "Terms":Terms,
        "academic_session":academic_session
        }
    return render(request, 'Publish_Result.html', context)

def getstudentsubjecttotals_view(request):
    data=json.loads(request.body)
    class_object = Class.objects.get(Class=data['studentclass'])
    term_object = Term.objects.get(term=data['selectedTerm'])
    session_object = AcademicSession.objects.get(session=data['selectedAcademicSession'])
    subjects_allocated = Subjectallocation.objects.filter(classname=class_object).first()
    students = Students_Pin_and_ID.objects.filter(student_class=class_object)
    final_list = []
    # get all the Students related to the Class
    for student in students:
        Resultdetails=Student_Result_Data.objects.filter(Student_name=student,Term=term_object,AcademicSession=session_object).first()
        student_dict = {
            'Name': student.student_name,
        }
        for subobject in subjects_allocated.subjects.all():
            try:
                subresult = Result.objects.get(student=student,students_result_summary=Resultdetails, Subject=subobject)
                student_dict[subobject.subject_code] = subresult.Total
            except:
                student_dict[subobject.subject_code] = "-"
        final_list.append(student_dict)
    return JsonResponse(final_list, safe=False)

def publishstudentresult_view(request):
    data=json.loads(request.body)
    termobject=data['classdata']['selectedTerm']
    Acadsessionobject=data['classdata']['selectedAcademicSession']
    Classdata=data['classdata']['studentclass']
    for studentdata in data['data']:
        classobject=Class.objects.get(Class=Classdata)
        resultterm = Term.objects.get(term=termobject)
        resultsession = AcademicSession.objects.get(session=Acadsessionobject)
        student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'])
        studentnumber=Students_Pin_and_ID.objects.filter(student_class=classobject).count()
        if Student_Result_Data.objects.filter(Student_name=student,Term=resultterm,AcademicSession=resultsession).exists():
            studentresult=Student_Result_Data.objects.get(Student_name=student,Term=resultterm,AcademicSession=resultsession)
            studentresult.TotalScore=studentdata['TOTAL']
            studentresult.Totalnumber= studentnumber
            studentresult.Average=studentdata['AVE']
            studentresult.Position=studentdata['POSITION']
            studentresult.Remark=studentdata['REMARK']
            studentresult.save()
        else:
            Student_Result_Data.objects.create(
            TotalScore=studentdata['TOTAL'],
            Average=studentdata['AVE'],
            Position=studentdata['POSITION'],
            Remark=studentdata['REMARK'],
            Student_name=student,
            Totalnumber= studentnumber,
            Term=resultterm,
            AcademicSession=resultsession
            )
    return JsonResponse('Results have been Published and its now open to the Students', safe=False)


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





