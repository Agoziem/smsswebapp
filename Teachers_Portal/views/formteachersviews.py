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
        "sessions": sessions
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
        sessionobject = get_object_or_404(
            AcademicSession, session=academic_session)

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
def PublishResults_view(request, Classname):
    Terms = Term.objects.all()
    academic_session = AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(
        classname=class_object).first()
    subject_code = []
    sessions = AcademicSession.objects.all()
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list': subject_code,
        "Terms": Terms,
        "academic_session": academic_session,
        "sessions": sessions
    }
    return render(request, 'formteachers/Publish_Result.html', context)

# Get the Students Subject Total


def getstudentsubjecttotals_view(request):
    try:
        data=json.loads(request.body)
        print(data)
        cls = Class.objects.get(Class=data['studentclass'])
        term = Term.objects.get(term=data['selectedTerm'])
        sess = AcademicSession.objects.get(session=data['selectedAcademicSession'])
        subjects_allocated = Subjectallocation.objects.filter(classname=cls).first()
        if not subjects_allocated:
            return JsonResponse({"error": "No subjects allocated to this class"}, status=400)
        
        students = StudentClassEnrollment.objects.filter(
            student_class=cls,
            academic_session=sess
        ).select_related("student")
        final_list = []
        # get all the Students related to the Class
        for student in students:
            Resultdetails,_=Student_Result_Data.objects.get_or_create(Student_name=student.student,Term=term,AcademicSession=sess)
            student_dict = {
                'id':student.student.id,
                'Name': student.student.student_name,
                'subjects':[],
            }
            for subobject in subjects_allocated.subjects.all():
                subject = {}
                try:
                    subresult = Result.objects.get(students_result_summary=Resultdetails, Subject=subobject)
                    subject['subject_code'] = subobject.subject_code
                    subject['subject_name'] = subobject.subject_name
                    subject['Total'] = subresult.Total
                    subject['published'] = subresult.published
                except:
                    subject['subject_code'] = subobject.subject_code
                    subject['subject_name'] = subobject.subject_name
                    subject['Total'] = "-"
                    subject['published'] = False
                student_dict['subjects'].append(subject)
            student_dict['published'] = Resultdetails.published
            final_list.append(student_dict)
        return JsonResponse(final_list, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    except (Class.DoesNotExist, Term.DoesNotExist, AcademicSession.DoesNotExist):
            return JsonResponse({"error": "Invalid class, term or session"}, status=400)
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": "An unexpected error occurred"},status=500)


# Publish the Students Results View


def publish_student_result_view(request):
    try:
        data = json.loads(request.body)
        term_object = Term.objects.get(term=data['classdata']['selectedTerm'])
        session_object = AcademicSession.objects.get(
            session=data['classdata']['selectedAcademicSession'])
        class_object = Class.objects.get(
            Class=data['classdata']['studentclass'])
        student_number = StudentClassEnrollment.objects.filter(
            student_class=class_object, academic_session=session_object).count()

        for student_data in data['data']:
            student_enrolled = StudentClassEnrollment.objects.get(
                student__student_name=student_data['Name'],
                student__id=student_data['id'],
                student_class=class_object,
                academic_session=session_object
            )

            student_result, created = Student_Result_Data.objects.get_or_create(
                Student_name=student_enrolled.student,
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
                student_result.Totalnumber = str(student_number)
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
        session_object = AcademicSession.objects.get(
            session=data['classdata']['selectedAcademicSession'])
        class_object = Class.objects.get(
            Class=data['classdata']['studentclass'])
        for student_data in data['data']:
            try:
                student_enrolled = StudentClassEnrollment.objects.get(
                    student__student_name=student_data['Name'],
                    student__id=student_data['id'],
                    student_class=class_object,
                    academic_session=session_object
                )
                student_result = Student_Result_Data.objects.get(
                    Student_name=student_enrolled.student,
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
def PublishAnnualResults_view(request, Classname):
    academic_session = AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(
        classname=class_object).first()
    subject_code = []
    sessions = AcademicSession.objects.all()
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list': subject_code,
        "academic_session": academic_session,
        "sessions": sessions
    }
    return render(request, 'formteachers/Annual_Publish_Result.html', context)


def annual_class_computation_view(request):
    data = json.loads(request.body)
    cls = Class.objects.get(Class=data['studentclass'])
    sess = AcademicSession.objects.get(session=data['selectedAcademicSession'])

    # 1) get all students in one go
    enrolls = (
        StudentClassEnrollment.objects
        .filter(student_class=cls, academic_session=sess)
        .select_related('student')
    )
    students = [e.student for e in enrolls]

    # 2) get allocation once
    alloc = Subjectallocation.objects.filter(
        classname=cls).prefetch_related('subjects').first()
    subjects = list(alloc.subjects.all()) if alloc else []

    # 3) bulk fetch all AnnualStudent rows
    annuals = AnnualStudent.objects.filter(
        Student_name__in=students, academicsession=sess
    ).select_related('Student_name')
    stu_to_annual = {
        a.Student_name.pk: a
        for a in annuals
    }

    # 4) bulk fetch all AnnualResult rows
    annual_results = AnnualResult.objects.filter(
        Student_name__in=annuals, Subject__in=subjects
    )
    result_map = {
        (r.Student_name.pk, r.Subject.pk): r
        for r in annual_results
    }

    # 5) build the output
    out = []
    for student in students:
        ann = stu_to_annual.get(student.id)
        published_flag = bool(ann and ann.published)# 3) bulk fetch existing AnnualStudent rows
    annuals_qs = AnnualStudent.objects.filter(
        Student_name__in=students,
        academicsession=sess
    ).select_related("Student_name")

    # Map existing by student‐PK
    stu_to_annual = { a.Student_name.pk: a for a in annuals_qs }

    # 3a) Figure out which student IDs are missing
    missing_ids = [
        stu.id
        for stu in students
        if stu.id not in stu_to_annual
    ]

    # 3b) Bulk‐create AnnualStudent for those
    to_create = [
        AnnualStudent(Student_name_id=stu_id, academicsession=sess)
        for stu_id in missing_ids
    ]
    AnnualStudent.objects.bulk_create(to_create)

    # 3c) Re‑fetch the newly created ones and merge into your map
    new_annuals = AnnualStudent.objects.filter(
        Student_name_id__in=missing_ids,
        academicsession=sess
    )
    for a in new_annuals:
        stu_to_annual[a.Student_name.pk] = a


    # Now stu_to_annual covers *all* students in your enrollment
    # ──────────────────────────────────────────────────────────────
    # 4) bulk fetch all AnnualResult rows the same way you did before
    annual_results = AnnualResult.objects.filter(
        Student_name__in=stu_to_annual.values(),
        Subject__in=subjects
    )
    result_map = {
        (r.Student_name.pk, r.Student_name.pk): r
        for r in annual_results
    }


    # 5) build the output
    out = []
    for student in students:
        ann = stu_to_annual[student.id]             
        published_flag = bool(ann.published)

        student_dict = {
            "Name":      student.student_name,
            "published": published_flag,
            "subjects":  [],
        }

        for subj in subjects:
            res = result_map.get((ann.pk, subj.id))
            student_dict["subjects"].append({
                "subject_code": subj.subject_code,
                "subject_name": subj.subject_name,
                "Average":      getattr(res, "Average", "-"),
                "published":    getattr(res,"published", False),
            })

        out.append(student_dict)

    return JsonResponse(out, safe=False)


def publish_annualstudentresult_view(request):
    try:
        data = json.loads(request.body)
        Acadsessionobject = data['classdata']['selectedAcademicSession']
        Classdata = data['classdata']['studentclass']
        for studentdata in data['data']:
            classobject = Class.objects.get(Class=Classdata)
            resultsession = AcademicSession.objects.get(
                session=Acadsessionobject)
            student = Students_Pin_and_ID.objects.get(
                student_name=studentdata['Name'])
            studentnumber = StudentClassEnrollment.objects.filter(
                student_class=classobject, academic_session=resultsession).count()
            try:
                studentresult = AnnualStudent.objects.get(
                    Student_name=student, academicsession=resultsession)
                studentresult.TotalScore = studentdata['Total']
                studentresult.Totalnumber = str(studentnumber)
                studentresult.Average = studentdata['Average']
                studentresult.Position = studentdata['Position']
                studentresult.Remark = studentdata['Remarks']
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
        return JsonResponse({"type": "danger", "message": "something went wrong, try again later"}, safe=False)


def unpublish_annual_classresults_view(request):
    data = json.loads(request.body)
    classobject = Class.objects.get(Class=data['classdata']['studentclass'])
    Acadsessionobject = AcademicSession.objects.get(
        session=data['classdata']['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(
        student_class=classobject, academic_session=Acadsessionobject)
    for student in students:
        try:
            studentresult = AnnualStudent.objects.get(
                Student_name=student.student, academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse({"type": "success", "message": "Results have been Unpublished and its now closed to the Students"}, safe=False)
