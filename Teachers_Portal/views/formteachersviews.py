from django.shortcuts import render
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json
from django.shortcuts import get_object_or_404

# /////////////////////////////////////////////
# Form teachers View for CRUD Students Details
@login_required
def Students_view(request, Classname, session_id):
    classobject = Class.objects.get(Class=Classname)
    sessionobject = AcademicSession.objects.get(id=session_id)
    sessions = AcademicSession.objects.all()
    # Fetch students enrolled in this class and session
    students = StudentClassEnrollment.objects.filter(
        student_class=classobject, academic_session=sessionobject
    ).select_related("student")  # Use select_related for optimized queries

    context = {
        "class": classobject,
        "session": sessionobject,
        "students": students,
        "sessions":sessions
    }
    return render(request, "formteachers/students.html", context)


# View to Create a new Student Record & enrollment Record
def createstudent_view(request):
    data = json.loads(request.body)
    student_name = data.get("studentname")
    student_sex = data.get("Student_sex")
    student_class = data.get("studentclass")
    academic_session = data.get("academicsession")

    try:
        # Fetch or validate class and session objects
        classobject = get_object_or_404(Class, Class=student_class)
        sessionobject = get_object_or_404(AcademicSession, session=academic_session)

        # Fetch or create the student record
        student, created = Students_Pin_and_ID.objects.get_or_create(
            student_name=student_name, Sex=student_sex
        )

        # Fetch or create the enrollment record
        enrollment, _ = StudentClassEnrollment.objects.get_or_create(
            student=student, student_class=classobject, academic_session=sessionobject
        )

        message = (
            f"{student.student_name} record has been {'created' if created else 'updated'} "
            f"successfully in {classobject.Class} for {sessionobject.session}."
        )

        return JsonResponse(
            {
                "student_ID": student.id,
                "student_id": student.student_id,
                "student_name": student.student_name,
                "student_sex": student.Sex,
                "message": message,
            },
            safe=False,
        )

    except Exception as e:
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False)


# View to Create a new Student Record & enrollment Record
def updatestudent_view(request):
    data = json.loads(request.body)
    student_id = data["studentID"]
    student_name = data["studentname"]
    student_sex = data["Student_sex"]
    student_class = data["studentclass"]
    academic_session = data["academicsession"]

    # Fetch class and session objects
    classobject = Class.objects.get(Class=student_class)
    sessionobject = AcademicSession.objects.get(session=academic_session)

    try:
        # Update the student record
        updateStudent = Students_Pin_and_ID.objects.get(id=student_id)
        updateStudent.student_name = student_name
        updateStudent.Sex = student_sex
        updateStudent.save()

        # Update or create the enrollment record
        enrollment, created = StudentClassEnrollment.objects.update_or_create(
            student=updateStudent,
            academic_session=sessionobject,
            defaults={"student_class": classobject},
        )

        context = {
            "student_ID": updateStudent.id,
            "student_id": updateStudent.student_id,
            "student_name": updateStudent.student_name,
            "student_sex": updateStudent.Sex,
            "message": f"{updateStudent.student_name}'s record has been updated successfully for {classobject.Class} in {sessionobject.session}.",
        }
        return JsonResponse(context, safe=False)
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False)


# View to Delete enrollment Record
def DeleteStudents_view(request):
    studentidstodelete = json.loads(request.body)
    studentnamesdeleted = []

    try:
        for student_id in studentidstodelete:
            # Fetch the student
            student = Students_Pin_and_ID.objects.get(id=student_id)
            
            # Delete their enrollment records
            StudentClassEnrollment.objects.filter(student=student).delete()
            studentnamesdeleted.append(student.student_name)

        context = {
            "message": f"The records for {studentnamesdeleted} have been deleted successfully."
        }
        return JsonResponse(context, safe=False)
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False)



# ------------------------------------------
# Form teachers View for submitting Results
# ------------------------------------------
@login_required
def PublishResults_view(request,Classname):
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    sessions = AcademicSession.objects.all()
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list':subject_code,
        "Terms":Terms,
        "academic_session":academic_session,
        "sessions":sessions
        }
    return render(request, 'formteachers/Publish_Result.html', context)

# Get the Students Subject Total
def getstudentsubjecttotals_view(request):
    try:
        data = json.loads(request.body)
        class_object = Class.objects.get(Class=data['studentclass'])
        term_object = Term.objects.get(term=data['selectedTerm'])
        session_object = AcademicSession.objects.get(session=data['selectedAcademicSession'])
        
        subjects_allocated = Subjectallocation.objects.filter(classname=class_object).first()
        if not subjects_allocated:
            return JsonResponse({"error": "No subjects allocated to this class"}, status=400)

        students = StudentClassEnrollment.objects.filter(
            student_class=class_object,
            academic_session=session_object
        ).select_related("student")

        final_list = []

        for student in students:
            result_details = Student_Result_Data.objects.filter(
                Student_name=student.student, 
                Term=term_object, 
                AcademicSession=session_object
            ).first()

            student_dict = {
                'Name': student.student.student_name,
                'subjects': [],
                'published': result_details.published if result_details else False,
            }

            for subobject in subjects_allocated.subjects.all():
                subject = {
                    'subject_code': subobject.subject_code,
                    'subject_name': subobject.subject_name,
                    'Total': "-",
                    'published': False
                }
                try:
                    subresult = Result.objects.get(
                        student=student.student,
                        students_result_summary=result_details,
                        Subject=subobject
                    )
                    subject['Total'] = subresult.Total
                    subject['published'] = subresult.published
                except Result.DoesNotExist:
                    pass

                student_dict['subjects'].append(subject)

            final_list.append(student_dict)

        return JsonResponse(final_list, safe=False)

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"error": "An error occurred while fetching student subject totals"}, status=500)

# Publish the Students Results View /// Continue from here 
def publish_student_result_view(request):
    try:
        data = json.loads(request.body)
        term_object = Term.objects.get(term=data['classdata']['selectedTerm'])
        session_object = AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
        class_object = Class.objects.get(Class=data['classdata']['studentclass'])

        student_number = StudentClassEnrollment.objects.filter(student_class=class_object,academic_session=session_object).count()

        for student_data in data['data']:
            student = Students_Pin_and_ID.objects.get(
                student_name=student_data['Name']
            )

            student_result, created = Student_Result_Data.objects.get_or_create(
                Student_name=student,
                Term=term_object,
                AcademicSession=session_object,
                defaults={
                    'TotalScore': student_data['Total'],
                    'Totalnumber': student_number,
                    'Average': student_data['Ave'],
                    'Position': student_data['Position'],
                    'Remark': student_data['Remarks'],
                    'published': True,
                }
            )
            if not created:
                # Update existing record
                student_result.TotalScore = student_data['Total']
                student_result.Totalnumber = student_number
                student_result.Average = student_data['Ave']
                student_result.Position = student_data['Position']
                student_result.Remark = student_data['Remarks']
                student_result.published = True
                student_result.save()

        return JsonResponse({
            "type": "success",
            "message": "Results have been published and are now open to the students"
        })

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({
            "type": "error",
            "message": "An error occurred while publishing student results"
        }, status=500)


def unpublish_classresults_view(request):
    try:
        data = json.loads(request.body)
        term_object = Term.objects.get(term=data['classdata']['selectedTerm'])
        session_object = AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
        class_object = Class.objects.get(Class=data['classdata']['studentclass'])

        for student_data in data['data']:
            try:
                student = Students_Pin_and_ID.objects.get(
                    student_name=student_data['Name']
                )
                student_result = Student_Result_Data.objects.get(
                    Student_name=student,
                    Term=term_object,
                    AcademicSession=session_object
                )
                student_result.published = False
                student_result.save()

            except Students_Pin_and_ID.DoesNotExist:
                print(f"Student not found: {student_data['Name']}")
                continue
            except Student_Result_Data.DoesNotExist:
                print(f"No result found for student: {student_data['Name']}")
                continue

        return JsonResponse({
            "type": "success",
            "message": "Results have been unpublished and are now closed to the students"
        })

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({
            "type": "error",
            "message": "An error occurred while unpublishing class results"
        }, status=500)




# -----------------------------------------------------------------------------------
# Annual views for the Form teachers
# -----------------------------------------------------------------------------------
@login_required
def PublishAnnualResults_view(request,Classname):
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    sessions = AcademicSession.objects.all()
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list':subject_code,
        "academic_session":academic_session,
        "sessions":sessions
        }
    return render(request, 'formteachers/Annual_Publish_Result.html', context)


def annual_class_computation_view(request):
    data=json.loads(request.body)
    classobject=Class.objects.get(Class=data['studentclass'])
    Acadsessionobject=AcademicSession.objects.get(session=data['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(
            student_class=classobject,
            academic_session=Acadsessionobject
        ).select_related("student")
    subjects_allocated = Subjectallocation.objects.filter(classname=classobject).first()
    final_list = []
    published = False
    for student in students:
        studentdict={
            'Name':student.student.student_name,
            "subjects":[]
        }
        for subobject in subjects_allocated.subjects.all():
            subject = {}
            try:
                subject_object = Subject.objects.get(subject_code=subobject.subject_code)
                studentAnnual = AnnualStudent.objects.get(Student_name=student.student, academicsession=Acadsessionobject)
                subjectAnnual = AnnualResult.objects.get(Student_name=studentAnnual, Subject=subject_object)
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Average'] = subjectAnnual.Average
                subject['published'] = studentAnnual.published
                published = studentAnnual.published
            except:
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Average'] = "-"
                subject['published'] = False
                published = False
            studentdict['published'] = published
            studentdict['subjects'].append(subject)
        final_list.append(studentdict)
    return JsonResponse(final_list, safe=False)

def publish_annualstudentresult_view(request):
    try:
        data=json.loads(request.body)
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        for studentdata in data['data']:
            classobject=Class.objects.get(Class=Classdata)
            resultsession = AcademicSession.objects.get(session=Acadsessionobject)
            student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'])
            studentnumber = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=resultsession).count()
            try:
                studentresult=AnnualStudent.objects.get(Student_name=student,academicsession=resultsession)
                studentresult.TotalScore=studentdata['Total']
                studentresult.Totalnumber= studentnumber
                studentresult.Average=studentdata['Average']
                studentresult.Position=studentdata['Position']
                studentresult.Remark=studentdata['Remarks']
                studentresult.Verdict = studentdata['Verdict']
                studentresult.published = True
                studentresult.save()
            except Exception as e:
                print(str(e))
                continue
        return JsonResponse({
            "type": "success",
            "message": "Annual Results have been published and are now opened to the Students"
            }, safe=False)
    except:
        return JsonResponse({"type":"danger","message":"something went wrong, try again later" }, safe=False)
    

def unpublish_annual_classresults_view(request):
    data=json.loads(request.body)
    classobject=Class.objects.get(Class=data['classdata']['studentclass'])
    Acadsessionobject=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=Acadsessionobject)
    for student in students:
        try:
            studentresult=AnnualStudent.objects.get(Student_name=student.student,academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse({"type":"success","message":"Results have been Unpublished and its now closed to the Students"}, safe=False)




