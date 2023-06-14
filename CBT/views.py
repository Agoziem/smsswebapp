from django.shortcuts import render
from .models import ExamClass, Subject, Teacher, QuestionSet, Question, Answer, CBTQuestions
from Result_portal.models import Students_Pin_and_ID,Class
from django.http import JsonResponse
from django.contrib import messages

def Teachers_cbt_authentication(request):
    if request.method == 'POST':
        teachers_id = request.POST['teachers_id']
        teachers_password = request.POST['teachers_password']
        try:
            teacher = Teacher.objects.get(teachers_id=teachers_id, teachers_password=teachers_password)
            exam_classes = ExamClass.objects.all()
            subjects = Subject.objects.all()
            teachers = Teacher.objects.all()
            context={
                "teacher":teacher,
                'exam_classes':exam_classes,
                'subjects': subjects,
                'teachers': teachers
            }
			# If form teacher exists, redirect to success page
            return render(request, 'Add_Questions.html', context)
        except Teacher.DoesNotExist:
			# If form teacher does not exist, display error message
            error_message = 'Check your input and try again'
            context={
                "error_message":error_message,
            }
            return render(request, 'teachers_CBT_page.html',context)

    context={
        
    }
    return render(request,"teachers_CBT_page.html",context)

def add_questionset(request):
    if request.method == 'POST':
        exam_class_id = request.POST.get('exam_class')
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        question_set_name = request.POST.get('question_set_name')
        question_texts = request.POST.getlist('question_text[]')
        answer_texts = request.POST.getlist('answer_text[]')
        correct_answers = request.POST.getlist('correct_answer[]')

        print(question_texts)
        print(answer_texts)
        print(correct_answers)
        # get exam class, subject, and teacher objects from their IDs
        exam_class = ExamClass.objects.get(id=exam_class_id)
        subject = Subject.objects.get(id=subject_id)
        teacher = Teacher.objects.get(id=teacher_id)

        # create the question set object
        question_set = QuestionSet.objects.create(name=question_set_name, subject=subject, exam_class=exam_class, teacher=teacher)

        # create question and answer objects and link them to the question set
        for i, question_text in enumerate(question_texts):
            question = Question.objects.create(text=question_text, question_set=question_set)
            # answer = Answer.objects.create(text=answer_texts[i], question=question, is_correct=correct_answers[i])

        return render(request, 'success.html')

    # else:
    #     exam_classes = ExamClass.objects.all()
    #     subjects = Subject.objects.all()
    #     teachers = Teacher.objects.all()
    #     return render(request, 'Add_Questions.html', {'exam_classes': exam_classes, 'subjects': subjects, 'teachers': teachers})

def get_Students(request, Classname):
    Students = Students_Pin_and_ID.objects.filter(student_class=Classname)
    Students_list = list(Students.values('id', 'student_name'))
    return JsonResponse(Students_list, safe=False)

def CBT_view(request):
    classes=Class.objects.all()
    if request.method == 'POST':
        student_name=str(request.POST['student_name'])
        student_id=str(request.POST['student_id'])
        try:
            student = Students_Pin_and_ID.objects.get(student_name=student_name,student_id=student_id)
            studentClass=Class.objects.get(Class=student.student_class)
            Exam_link = CBTQuestions.objects.get(StudentClass=studentClass.id)
            context={
                'exam_link':Exam_link,
                'student': student,
                'studentClass':studentClass,
            }
			# If form teacher exists, redirect to success page
            return render(request, 'Start_Exam.html', context)
        except Students_Pin_and_ID.DoesNotExist:
            classes=Class.objects.all()
			# If form teacher does not exist, display error message
            context={
                "classes":classes,
            }
            messages.error(request, 'Check your Student id or the Pin and try again , make sure you are entering it Correctly')
            return render(request, 'CBT_center.html',context)

    context={
			"classes":classes
		}
    return render(request,"CBT_center.html",context)