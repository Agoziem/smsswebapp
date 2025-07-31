from django.shortcuts import render, get_object_or_404
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json
from django.views.decorators.http import require_POST



#-------------------------------------- 
# Teachers Result Formulation Part
# -------------------------------------
@login_required
def result_computation_view(request, Classname, id):
    teacher = Teacher.objects.get(id=id)
    Terms = Term.objects.all()
    academic_session = AcademicSession.objects.all()
    classobject = get_object_or_404(Class, Class=Classname)
    subjectsforclass = get_object_or_404(Subjectallocation, classname=classobject)
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
    data=json.loads(request.body)
    classobject = get_object_or_404(Class, Class=data['studentclass'])
    subjectobject = get_object_or_404(Subject, subject_name=data['studentsubject'])
    term = get_object_or_404(Term, term=data['selectedTerm'])
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])
    enrollments = StudentClassEnrollment.objects.filter(student_class=classobject, academic_session=session).select_related('student')
    studentResults = []

    for enrollment in enrollments:
        student_result_details, _ = Student_Result_Data.objects.get_or_create(Student_name=enrollment.student, Term=term, AcademicSession=session)
        student_result_object, _ = Result.objects.get_or_create(student=enrollment.student, Subject=subjectobject, students_result_summary=student_result_details, student_class=classobject)
        try:
            total_test_score = TestQuestionSet.objects.get(
                testSubject=subjectobject, testSetGroup__student=enrollment.student
            )
            student_result_object.MidTermTest = str(total_test_score.testTotalScore)
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
    return JsonResponse(studentResults, safe=False, status=200)

@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    classobject= get_object_or_404(Class, Class=data['classdata']['studentclass'])
    term=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
    session= get_object_or_404(AcademicSession, session=data['classdata']['selectedSession'])
    subjectobject = get_object_or_404(Subject, subject_name=data['classdata']['selectedSubject'])
    studentobject= get_object_or_404(Students_Pin_and_ID, student_id=data['formDataObject']['studentID'], student_name=data['formDataObject']['Name'])
    student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject, Term=term, AcademicSession=session)
    studentResult = get_object_or_404(Result, student=studentobject, students_result_summary=student_result_details, Subject=subjectobject, student_class=classobject)
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
    term=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
    session=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    classobject= get_object_or_404(Class, Class=data['classdata']['studentclass'])
    subjectobject = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    for result in data['data']:
        studentobject= get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'],student_name=result['Name'])
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
        studentobject= get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'],student_name=result['Name'])
        student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject,Term=term,AcademicSession=session)
        studentResult = get_object_or_404(Result, student=studentobject,students_result_summary=student_result_details,student_class=classobject,Subject=subject)
        studentResult.published=False
        studentResult.save()
    return JsonResponse('Results Unpublished Successfully', safe=False)


# ---------------------------------
# Annual Result Computation Views
# ---------------------------------
def annualresult_computation(request,Classname,id):
    teacher = get_object_or_404(Teacher, id=id)
    academic_session= AcademicSession.objects.all()
    classobject = get_object_or_404(Class, Class=Classname)
    subjectsforclass= get_object_or_404(Subjectallocation, classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))
    context={
        'class':classobject,
        "academic_session":academic_session,
        "subjects_taught_for_class":subjects_taught_for_class,
        "session":academic_session,
         "sessions":academic_session
        } 
    return render(request,'teachers/Annual_Results.html',context)

@login_required
@require_POST
def annual_result_computation_view(request):
    data = json.loads(request.body)
    
    class_obj = get_object_or_404(Class, Class=data['studentclass'])
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])
    subject = get_object_or_404(Subject, subject_name=data['studentsubject'])
    
    students = StudentClassEnrollment.objects.filter(
        student_class=class_obj, academic_session=session
    )
    terms = Term.objects.all()
    
    result_data = []

    for enrollment in students:
        student = enrollment.student
        student_annual, _ = AnnualStudent.objects.get_or_create(
            Student_name=student, academicsession=session
        )
        annual_result, _ = AnnualResult.objects.get_or_create(
            Student_name=student_annual, Subject=subject
        )
        
        term_totals = {}
        for term in terms:
            try:
                result_summary, _ = Student_Result_Data.objects.get_or_create(
                    Student_name=student, Term=term, AcademicSession=session
                )
                result_obj, _ = Result.objects.get_or_create(
                    students_result_summary=result_summary, Subject=subject
                )
                term_totals[term.term] = result_obj.Total
            except Exception as e:
                print(f"[{student.student_name}] {term.term} error: {e}")
                term_totals[term.term] = '-'
        
        result_data.append({
            'studentID': student.student_id,
            'Name': student.student_name,
            'terms': term_totals,
            'published': annual_result.published
        })

    return JsonResponse(result_data, safe=False, status=200)


def publish_annual_results(request):
    data = json.loads(request.body)
    session = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    subject_object = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
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
    session = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    subject_object = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    for studentdata in data['data']:
        student = get_object_or_404(Students_Pin_and_ID, student_name=studentdata['Name'], student_id=studentdata['studentID'])
        studentAnnual = get_object_or_404(AnnualStudent, Student_name=student, academicsession=session)
        student_annual_details = get_object_or_404(AnnualResult, Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.published = False
        student_annual_details.save()
    return JsonResponse('Results have been unpublished', safe=False)
    
    

