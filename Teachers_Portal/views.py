from django.shortcuts import render, redirect, get_object_or_404
from Result_portal.models import Students_Pin_and_ID,Class,Subject
from .models import *
from django.http import JsonResponse
from .forms import TeacherForm
from django.contrib.auth.decorators import login_required
from CBT.models import *
import json


@login_required
def Teachers_dashboard_view(request):
    context={

    }
    return render(request,'Teachers_dashboard.html',context)

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

@login_required
def result_computation_view(request,Classname):
    classobject = Class.objects.get(Class=Classname)
    context={
        'class':classobject
        } 
    return render(request,'Result_computation.html',context)

@login_required
def CBT_Questions_view(request,teachers_id):
    subjects=Subject.objects.all()
    classes=Class.objects.all()
    teacher=Teacher.objects.get(id=teachers_id)
    if request.method == 'POST':
        classname=request.POST['test_classes']
        subject=Subject.objects.get(id=request.POST['subject'])
        time=request.POST['testTime']
        questionset,created=QuestionSet.objects.get_or_create(
            subject=subject,
            examTime=time,
            teacher=teacher
        )
        for class_id in classname:
            class_object = Class.objects.get(id=class_id)
            class_object.save()
            questionset.ExamClass.add(class_object) 
        questionset.save()
        context={
        'questionSet':questionset
        }
        return render(request,'CBT_Questions.html',context)
    context={
        "subjects":subjects,
        "classes":classes,
        "teacher":teacher
    }
    return render(request,'CBT_details.html',context)

def CBT_update_details(request,id):
    questionset = QuestionSet.objects.get(id=id)
    if request.method == 'POST':
        classname=request.POST['test_classes']
        time=request.POST['testTime']
        questionset.examTime = time
        questionset.ExamClass.clear()
        for class_id in classname:
            class_object = Class.objects.get(id=class_id)
            class_object.save()
            questionset.ExamClass.add(class_object) 
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
        classes = data['Class']

        # Get or create Subject and Teacher instances
        subject = Subject.objects.get(subject_name=subject_name)
        teacher = Teacher.objects.get(FirstName=teacher_name)

        # Create the QuestionSet
        question_set,created = QuestionSet.objects.get_or_create(
            examTime=exam_time,
            teacher=teacher,
            subject=subject
        )

        # Process the list of questions
        questions_data = data['questions']
        for question_data in questions_data:
            question_text = question_data.get('questionText')
            question_mark = question_data.get('questionMark')
            required = question_data.get('questionrequired')

            # Create the Question
            question,created = Question.objects.get_or_create(
                questiontext=question_text,
                questionMark=question_mark,
            )
            question.required=required
            question.save()
            # Process answers for the current question
            answers_data = question_data['answers']
            for answer_data in answers_data:
                answer_text = answer_data.get('answerText')
                is_correct = answer_data.get('isCorrect')

                # Create the Answer
                answer,created = Answer.objects.get_or_create(
                    answertext=answer_text,
                )
                answer.isCorrect=is_correct
                answer.save()
                # Add the answer to the question's ManyToManyField
                question.answers.add(answer)

            # Add the question to the QuestionSet's ManyToManyField
            question_set.questions.add(question)

        # Add the selected classes to the QuestionSet
        for class_name in classes:
            class_obj, created = Class.objects.get_or_create(Class=class_name)
            question_set.ExamClass.add(class_obj)

        return JsonResponse({'success': 'Data saved successfully'})  # Return a success response

    return JsonResponse({'error': 'Invalid request method'})


@login_required
def CBT_result_view(request):
    context={

    }
    return render(request,'CBT_results.html',context)

@login_required
def Students_view(request,Classname):
    classobject = Class.objects.get(Class=Classname)
    context={
        'class':classobject
        } 
    return render(request,'students.html',context)


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





