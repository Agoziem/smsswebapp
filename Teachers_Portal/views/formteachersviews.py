from django.shortcuts import render,get_object_or_404
from requests import get
from Result_portal.models import *
from ..models import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json
from django.shortcuts import get_object_or_404
from itertools import islice

# /////////////////////////////////////////////
# Form teachers View for CRUD Students Details


@login_required
def Students_view(request, Classname, session_id):
    classobject = get_object_or_404(Class, Class=Classname)
    sessionobject = get_object_or_404(AcademicSession, id=session_id)
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
                "student_ID": student.pk,
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
    classobject = get_object_or_404(Class, Class=student_class)
    sessionobject = get_object_or_404(AcademicSession, session=academic_session)

    try:
        # Update the student record
        updateStudent = get_object_or_404(Students_Pin_and_ID, id=student_id)
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
            "student_ID": updateStudent.pk,
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
    class_object = get_object_or_404(Class, Class=Classname)
    subjects_allocation = get_object_or_404(Subjectallocation, classname=class_object)
    sessions = AcademicSession.objects.all()
    subject_code = []
    if not subjects_allocation:
        return render(request, 'No_Subjects_Allocated.html',{"class": class_object})
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list': subject_code,
        "Terms": Terms,
        "academic_session": sessions,
        "sessions": sessions
    }
    return render(request, 'formteachers/Publish_Result.html', context)

# Get the Students Subject Total


def getstudentsubjecttotals_view(request):
    try:
        data=json.loads(request.body)
        cls = get_object_or_404(Class, Class=data['studentclass'])
        term = get_object_or_404(Term, term=data['selectedTerm'])
        sess = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])
        subjects_allocated = get_object_or_404(Subjectallocation, classname=cls)
        if not subjects_allocated:
            return JsonResponse({"error": "No subjects allocated to this class"}, status=400)
        
        students = StudentClassEnrollment.objects.filter(
            student_class=cls,
            academic_session=sess
        ).select_related("student")

        # 1. Get or create summaries in bulk (avoid calling get_or_create in loop)
        existing_summaries = Student_Result_Data.objects.filter(
            Student_name__in=[s.student for s in students],
            Term=term,
            AcademicSession=sess
        )
        summary_map = {s.Student_name.pk: s for s in existing_summaries}

        # Determine which are missing
        missing_students = [s.student for s in students if s.student.pk not in summary_map]
        Student_Result_Data.objects.bulk_create([
            Student_Result_Data(Student_name=stu, Term=term, AcademicSession=sess)
            for stu in missing_students
        ])

        # Re-fetch all summaries again
        all_summaries = Student_Result_Data.objects.filter(
            Student_name__in=[s.student for s in students],
            Term=term,
            AcademicSession=sess
        )
        summary_map = {s.Student_name.pk: s for s in all_summaries}

        # 2. Bulk fetch all relevant Results in one query ie (no of subjects allocated * number of students)
        result_map = {}
        batch_size = 5000  # or any safe value depending on your instance size
        results_iterator = Result.objects.filter(
            students_result_summary__in=all_summaries,
            Subject__in=subjects_allocated.subjects.all()
        ).select_related(
            "Subject", "students_result_summary", "students_result_summary__Student_name"
        ).iterator(chunk_size=batch_size)

        # 3. Build a result lookup
        for r in results_iterator:
            if not r.students_result_summary or not r.Subject:
                continue
            result_map[(r.students_result_summary.Student_name.pk, r.Subject.pk)] = r

        # 4. Construct final_list
        final_list = []
        for enrollment in students:
            student = enrollment.student
            summary = summary_map.get(student.id)
            if not summary:
                continue

            student_dict = {
                "id": student.id,
                "Name": student.student_name,
                "published": summary.published,
                "subjects": []
            }

            for subject in subjects_allocated.subjects.all():
                key = (student.id, subject.id)
                result = result_map.get(key)
                student_dict["subjects"].append({
                    "subject_code": subject.subject_code,
                    "subject_name": subject.subject_name,
                    "Total": result.Total if result else "-",
                    "published": result.published if result else False
                })

            final_list.append(student_dict)

        return JsonResponse(final_list, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": "An unexpected error occurred"},status=500)


# Publish the Students Results View


def publish_student_result_view(request):
    try:
        data = json.loads(request.body)
        term_object = get_object_or_404(Term, term=data['classdata']['selectedTerm'])
        session_object = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        class_object = get_object_or_404(Class, Class=data['classdata']['studentclass'])
        student_number = StudentClassEnrollment.objects.filter(
            student_class=class_object, academic_session=session_object).count()

        for student_data in data['data']:
            student_enrolled = get_object_or_404(StudentClassEnrollment,
                student__student_name=student_data['Name'],
                student__id=student_data['id'],
                student_class=class_object,
                academic_session=session_object
            )
            # Create or update the student result data
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
        }, status=200)

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({
            "type": "error",
            "message": "An error occurred while publishing student results"
        }, status=500)


def unpublish_classresults_view(request):
    try:
        data = json.loads(request.body)
        term_object = get_object_or_404(Term, term=data['classdata']['selectedTerm'])
        session_object = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        class_object = get_object_or_404(Class, Class=data['classdata']['studentclass'])
        for student_data in data['data']:
            try:
                student_enrolled = get_object_or_404(StudentClassEnrollment,
                    student__student_name=student_data['Name'],
                    student__id=student_data['id'],
                    student_class=class_object,
                    academic_session=session_object
                )
                student_result = get_object_or_404(Student_Result_Data,
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
    class_object = get_object_or_404(Class, Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    sessions = AcademicSession.objects.all()
    subject_code = []
    if not subjects_allocation:
        return render(request, 'No_Subjects_Allocated.html', {"class": class_object})
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
    cls = get_object_or_404(Class, Class=data['studentclass'])
    sess = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])

    enrolls = (
        StudentClassEnrollment.objects
        .filter(student_class=cls, academic_session=sess)
        .select_related('student')
    )
    students = [e.student for e in enrolls]

    alloc = Subjectallocation.objects.filter(
        classname=cls
    ).prefetch_related('subjects').first()

    subjects = list(alloc.subjects.all()) if alloc else []

    annuals = AnnualStudent.objects.filter(
        Student_name__in=students,
        academicsession=sess
    ).select_related('Student_name')

    stu_to_annual = {a.Student_name.pk: a for a in annuals}

    # Create missing AnnualStudent records
    missing_ids = [s.id for s in students if s.id not in stu_to_annual]
    AnnualStudent.objects.bulk_create([
        AnnualStudent(Student_name_id=stu_id, academicsession=sess)
        for stu_id in missing_ids
    ])

    new_annuals = AnnualStudent.objects.filter(
        Student_name_id__in=missing_ids,
        academicsession=sess
    )
    for a in new_annuals:
        stu_to_annual[a.Student_name.pk] = a

    # Bulk fetch annual results
    annual_results = AnnualResult.objects.filter(
        Student_name__in=stu_to_annual.values(),
        Subject__in=subjects
    )
    result_map = {
        (r.Student_name.pk, r.Subject.pk): r
        for r in annual_results
    }

    # Build response
    out = []
    for student in students:
        ann = stu_to_annual[student.id]
        student_dict = {
            "Name": student.student_name,
            "published": bool(ann.published),
            "subjects": [],
        }
        for subj in subjects:
            res = result_map.get((ann.pk, subj.pk))
            student_dict["subjects"].append({
                "subject_code": subj.subject_code,
                "subject_name": subj.subject_name,
                "Average": getattr(res, "Average", "-"),
                "published": getattr(res, "published", False),
            })
        out.append(student_dict)

    return JsonResponse(out, safe=False)



def publish_annualstudentresult_view(request):
    try:
        data = json.loads(request.body)
        classobject = get_object_or_404(Class, Class=data['classdata']['studentclass'])
        resultsession = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        studentnumber = StudentClassEnrollment.objects.filter(
            student_class=classobject, academic_session=resultsession).count()
        for studentdata in data['data']:
            student = get_object_or_404(Students_Pin_and_ID, student_name=studentdata['Name'])
            try:
                studentresult = get_object_or_404(
                    AnnualStudent, Student_name=student, academicsession=resultsession)
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
    classobject = get_object_or_404(Class, Class=data['classdata']['studentclass'])
    Acadsessionobject = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(
        student_class=classobject, academic_session=Acadsessionobject)
    for student in students:
        try:
            studentresult = get_object_or_404(AnnualStudent, Student_name=student.student, academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse({"type": "success", "message": "Results have been Unpublished and its now closed to the Students"}, safe=False)
