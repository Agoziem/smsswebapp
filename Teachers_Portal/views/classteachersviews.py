from django.shortcuts import render, redirect, get_object_or_404
from requests import get
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json


#-------------------------------------- 
# Teachers Result Formulation Part
# -------------------------------------
@login_required
def result_computation_view(request,Classname,id):
    teacher = Teacher.objects.get(id=id)
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    classobject = get_object_or_404(Class,Class=Classname)
    subjectsforclass=get_object_or_404(Subjectallocation,classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))

    context={
            'class':classobject,
            "Terms":Terms,
            "academic_session":academic_session,
            "subjects_taught_for_class":subjects_taught_for_class,
           "sessions":academic_session
        }
    return render(request,'teachers/Result_computation.html',context)

@login_required
def get_students_result_view(request):
    data = json.loads(request.body)
    
    # Fetch related objects
    classobject = get_object_or_404(Class, Class=data['studentclass'])
    subjectobject = get_object_or_404(Subject, subject_name=data['studentsubject'])
    term = get_object_or_404(Term, term=data['selectedTerm'])
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])

    # Fetch enrolled students for the class and session
    students_qs = StudentClassEnrollment.objects.select_related('student').filter(
        student_class=classobject,
        academic_session=session
    )
    students = list(students_qs)
    student_ids = [s.student.pk for s in students]

    # Prefetch Student_Result_Data and Results in bulk
    result_data_map = {
        (r.Student_name.pk): r for r in Student_Result_Data.objects.filter(
            Student_name__in=student_ids,
            Term=term,
            AcademicSession=session
        )
    }

    result_map = {
        (r.student.pk): r for r in Result.objects.filter(
            student_id__in=student_ids,
            Subject=subjectobject,
            student_class=classobject,
            students_result_summary__in=result_data_map.values()
        ).select_related("student", "students_result_summary")
    }

    test_scores = {
        t.testSetGroup.student.pk: t.testTotalScore
        for t in TestQuestionSet.objects.select_related("testSetGroup__student").filter(
            testSubject=subjectobject,
            testSetGroup__student__in=student_ids
        )
    }

    studentResults = []

    for s in students:
        student = s.student
        student_result_data = result_data_map.get(student.pk)
        if not student_result_data:
            student_result_data = Student_Result_Data.objects.create(
                Student_name=student, Term=term, AcademicSession=session
            )
            result_data_map[student.pk] = student_result_data

        student_result = result_map.get(student.pk)
        if not student_result:
            student_result = Result.objects.create(
                student=student,
                Subject=subjectobject,
                students_result_summary=student_result_data,
                student_class=classobject
            )
            result_map[student.pk] = student_result

        test_score = test_scores.get(student.pk)
        if test_score is not None:
            student_result.MidTermTest = str(test_score)

        studentResults.append({
            'Name': student.student_name,
            'studentID': student.student_id,
            '1sttest': student_result.FirstTest,
            '1stAss': student_result.FirstAss,
            'MidTermTest': student_result.MidTermTest,
            '2ndTest': student_result.SecondAss,
            '2ndAss': student_result.SecondTest,
            'Exam': student_result.Exam,
            'published': student_result.published,
        })

    return JsonResponse(studentResults, safe=False)


@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['selectedSubject'] 
    Classdata=data['classdata']['selectedClass']
    studentID=data['formDataObject']['studentID']
    Name=data['formDataObject']['Name']
    classobject= Class.objects.get(Class=Classdata)
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedSession'])
    studentobject= Students_Pin_and_ID.objects.get(student_id=studentID,student_name=Name)
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
    term=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
    session=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    classobject= get_object_or_404(Class, Class=Classdata)
    subjectobject = get_object_or_404(Subject, subject_name=subject)
    for result in data['data']:
        studentobject= get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'], student_name=result['Name'])
        student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject, Term=term, AcademicSession=session)
        studentResult = get_object_or_404(Result, student=studentobject, students_result_summary=student_result_details, Subject=subjectobject, student_class=classobject)
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
    term=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
    session=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    classobject= get_object_or_404(Class, Class=data['classdata']['studentclass'])
    subject = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    for result in data['data']:
        studentobject= get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'], student_name=result['Name'])
        student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject, Term=term, AcademicSession=session)
        studentResult = get_object_or_404(Result, student=studentobject, students_result_summary=student_result_details, student_class=classobject, Subject=subject)
        studentResult.published=False
        studentResult.save()
    return JsonResponse('Results Unpublished Successfully', safe=False)


# ---------------------------------
# Annual Result Computation Views
# ---------------------------------
def annualresult_computation(request,Classname,id):
    teacher = Teacher.objects.get(id=id)
    academic_session= AcademicSession.objects.all()
    classobject = Class.objects.get(Class=Classname)
    subjectsforclass=Subjectallocation.objects.get(classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))
    context={
        'class':classobject,
        "academic_session":academic_session,
        "subjects_taught_for_class":subjects_taught_for_class,
        "session":academic_session,
         "sessions":academic_session
        } 
    return render(request,'teachers/Annual_Results.html',context)

def annual_result_computation_view(request):
    data = json.loads(request.body)
    subject_name = data['studentsubject']
    class_name = data['studentclass']
    academic_session = data['selectedAcademicSession']

    class_object = get_object_or_404(Class, Class=class_name)
    session = get_object_or_404(AcademicSession, session=academic_session)
    subject_object = get_object_or_404(Subject, subject_name=subject_name)

    # Prefetch all enrollments with related student
    student_enrollments = StudentClassEnrollment.objects.select_related('student').filter(
        student_class=class_object, academic_session=session
    )
    student_ids = [e.student.pk for e in student_enrollments]

    # Prefetch AnnualStudent in bulk
    annual_students = AnnualStudent.objects.filter(
        Student_name_id__in=student_ids,
        academicsession=session
    ).select_related('Student_name')
    annual_student_map = {a.Student_name.pk: a for a in annual_students}

    # Prefetch AnnualResults in bulk
    annual_results = AnnualResult.objects.filter(
        Student_name__in=annual_students,
        Subject=subject_object
    ).select_related('Student_name')
    annual_result_map = {
        (ar.Student_name.Student_name.pk): ar for ar in annual_results
    }

    # Prefetch Student_Result_Data
    srd_list = Student_Result_Data.objects.filter(
        Student_name__in=student_enrollments,
        Term__in=Term.objects.all(),
        AcademicSession=session
    ).select_related('Student_name', 'Term')

    srd_map = {}
    for srd in srd_list:
        srd_map[(srd.Student_name.pk, srd.Term.pk)] = srd # type: ignore

    # Prefetch Result entries
    result_qs = Result.objects.filter(
        students_result_summary__in=srd_list,
        Subject=subject_object
    ).select_related('students_result_summary', 'Subject')
    result_map = {
        (r.students_result_summary.Student_name.pk, r.students_result_summary.Term.pk): r # type: ignore
        for r in result_qs
    }

    terms = list(Term.objects.all())
    students_annuals = []

    for enrollment in student_enrollments:
        student = enrollment.student
        annual_student = annual_student_map.get(student.pk)
        if not annual_student:
            annual_student = AnnualStudent.objects.create(Student_name=student, academicsession=session)
            annual_student_map[student.pk] = annual_student

        annual_result = annual_result_map.get(student.pk)
        if not annual_result:
            annual_result = AnnualResult.objects.create(Student_name=annual_student, Subject=subject_object)
            annual_result_map[student.pk] = annual_result

        termsobject = {}
        for term in terms:
            srd = srd_map.get((student.pk, term.pk))
            if srd:
                result = result_map.get((student.pk, term.pk))
                termsobject[term.term] = result.Total if result else '-'
            else:
                termsobject[term.term] = '-'

        students_annuals.append({
            'studentID': student.student_id,
            'Name': student.student_name,
            'terms': termsobject,
            'published': annual_result.published
        })

    return JsonResponse(students_annuals, safe=False)



def publish_annual_results(request):
    data = json.loads(request.body)
    subject_name = data['classdata']['studentsubject']
    class_name = data['classdata']['studentclass']
    academic_session = data['classdata']['selectedAcademicSession']
    session = get_object_or_404(AcademicSession, session=academic_session)
    subject_object = get_object_or_404(Subject, subject_name=subject_name)
    for result in data['data']:
        student = get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'], student_name=result['Name'])
        studentAnnual = get_object_or_404(AnnualStudent, Student_name=student, academicsession=session)
        student_annual_details = get_object_or_404(AnnualResult, Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.FirstTermTotal = result["terms"]["1st Term"]
        student_annual_details.SecondTermTotal = result["terms"]["2nd Term"]
        student_annual_details.ThirdTermTotal = result["terms"]["3rd Term"]
        student_annual_details.Total = result['Total']
        student_annual_details.Average = result['Average']
        student_annual_details.Grade = result['Grade']
        student_annual_details.SubjectPosition = result['Position']
        student_annual_details.Remark = result['Remarks']
        student_annual_details.published = True
        student_annual_details.save()
    return JsonResponse('Results have been published', safe=False)


def unpublish_annual_results(request):
    data = json.loads(request.body)
    subject_name = data['classdata']['studentsubject']
    class_name = data['classdata']['studentclass']
    academic_session = data['classdata']['selectedAcademicSession']
    session = get_object_or_404(AcademicSession, session=academic_session)
    subject_object = get_object_or_404(Subject, subject_name=subject_name)
    for studentdata in data['data']:
        student = get_object_or_404(Students_Pin_and_ID, student_name=studentdata['Name'])
        studentAnnual = get_object_or_404(AnnualStudent, Student_name=student, academicsession=session)
        student_annual_details = get_object_or_404(AnnualResult, Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.published = False
        student_annual_details.save()
    return JsonResponse('Results have been unpublished', safe=False)
    
    

