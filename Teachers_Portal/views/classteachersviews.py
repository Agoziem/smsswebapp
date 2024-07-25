from django.shortcuts import render, redirect, get_object_or_404
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from ..forms import TeacherForm
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json
from django.db.models import Q




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
            'studentID': student_result_object.student.student_id,
            '1sttest': student_result_object.FirstTest,
            '1stAss': student_result_object.FirstAss,
            'MidTermTest': student_result_object.MidTermTest,
            '2ndTest': student_result_object.SecondAss,
            '2ndAss': student_result_object.SecondTest,
            'Exam': student_result_object.Exam,
            'published': student_result_object.published,
        })

    return JsonResponse(studentResults, safe=False)

@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['studentsubject']
    Classdata=data['classdata']['studentclass']
    studentID=data['formDataObject']['studentID']
    Name=data['formDataObject']['Name']
    classobject= Class.objects.get(Class=Classdata)
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    studentobject= Students_Pin_and_ID.objects.get(student_id=studentID,student_name=Name,student_class=classobject)
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
        studentobject= Students_Pin_and_ID.objects.get(student_id=result['studentID'],student_name=result['Name'])
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
        studentResult.published=True
        studentResult.save()
    return JsonResponse('Results submitted Successfully', safe=False)


def unpublish_results_view(request):
    data=json.loads(request.body)
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    classobject= Class.objects.get(Class=data['classdata']['studentclass'])
    subject = Subject.objects.get(subject_name=data['classdata']['studentsubject'])
    for result in data['data']:
        studentobject= Students_Pin_and_ID.objects.get(student_id=result['studentID'],student_name=result['Name'])
        student_result_details = Student_Result_Data.objects.get(Student_name=studentobject,Term=term,AcademicSession=session)
        studentResult = Result.objects.get(student=studentobject,students_result_summary=student_result_details,student_class=classobject,Subject=subject)
        studentResult.published=False
        studentResult.save()
    return JsonResponse('Results Unpublished Successfully', safe=False)



