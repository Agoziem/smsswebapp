from django.shortcuts import render
from Result_portal.models import Class,Students_Pin_and_ID,Result,Student_Result_Data
import json
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
from CBT.models import *
from django.db.models import F,Sum


def CBT_view(request):
    classobjects=Class.objects.all()
    testday = False
    if request.method == 'POST':
        classname=request.POST['student_class']
        studentname=request.POST['student_name']
        # time=request.POST['time']
        date=request.POST['date']
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        # time_obj = datetime.strptime(time, "%H:%M:%S").time()
        classobject=Class.objects.get(Class=classname)
        student=Students_Pin_and_ID.objects.get(student_name=studentname,student_class=classobject)
        try:
            questionGroup = QuestionSetGroup.objects.get(date=date_obj)
            testday = True
            questionSets=[]
            total_time=0
            for questionset in questionGroup.questionsets.all():
                if classobject in questionset.ExamClass.all():
                    total_time += questionset.examTime
                    questionSets.append(questionset)

            context={
            'total_time':total_time,
            'classobject':classobject,
            'student':student,
            'questionsetsgroup':questionSets,
            'testday': testday,
            'questionGroup':questionGroup,
        }
        except:
            testday = False
            context={
            'classobject':classobject,
            'student':student,
            'testday': testday,
        }
        
        return render(request,'Test_instructions.html',context)
    context={
        'classobjects':classobjects
    }
    return render(request,'CBT_center.html',context)


def test_view(request,student_id,class_id,questionGroup_id):
    student=Students_Pin_and_ID.objects.get(id=student_id)
    classobject=Class.objects.get(id=class_id)
    questionGroup=QuestionSetGroup.objects.get(id=questionGroup_id)
    total_time=0
    total_questions = 0
    questionSets=[]
    for questionset in questionGroup.questionsets.all():
        if classobject in questionset.ExamClass.all():
            total_time += questionset.examTime
            question_count = questionset.questions.count()
            total_questions += question_count
            questionSets.append(questionset)
    context={
        'total_questions':total_questions,
        'total_time':total_time,
        'classobject':classobject,
        'student':student,
        'questionsetsgroup':questionSets,
        'questionGroup':questionGroup,
    }
    return render(request,'Test.html',context)


def submit_test_view(request):
    test_data=json.loads(request.body)
    group_name = test_data['groupName']
    test_name = test_data['grouptestname']
    student_name = test_data['studentname']
    student_class = test_data['studentclass']
    question_sets = test_data['questionSets']

    classobject=Class.objects.get(Class=student_class)
    testobject=Test.objects.get(name=test_name)
    studentobject=Students_Pin_and_ID.objects.get(student_name=student_name)
    if not TestSetGroup.objects.filter(name=group_name,testClass=classobject,test=testobject,student=studentobject).exists():
        test_set_group,created = TestSetGroup.objects.get_or_create(
            name=group_name,
            testClass=classobject,
            test=testobject,
            student=studentobject
            )

        for question_set_data in question_sets:
            test_subject_name = question_set_data['testSubject']
            test_questionset_score=question_set_data['testTotalScore']
            test_total_score = int(test_questionset_score)
            subjectobject=Subject.objects.get(subject_name=test_subject_name)
            student_data,created=Student_Result_Data.objects.get_or_create(Student_name=studentobject)
            if Result.objects.filter(students_result_data=student_data,Subject=subjectobject).exists():
                student_result=Result.objects.get(students_result_data=student_data,Subject=subjectobject)
                student_result.MidTermTest=test_questionset_score
                student_result.save()
            else:
                student_result=Result.objects.create(students_result_data=student_data,Subject=subjectobject,MidTermTest=test_questionset_score)
            if TestQuestionSet.objects.filter(testSetGroup=test_set_group,testSubject=subjectobject).exists():
                test_question_set = TestQuestionSet.objects.get(
                    testSetGroup=test_set_group,
                    testSubject=subjectobject,
                    testTotalScore=test_total_score
                )
                test_question_set.testTotalScore=test_total_score
                test_question_set.save()
            else:
                test_question_set = TestQuestionSet.objects.create(
                    testSetGroup=test_set_group,
                    testSubject=subjectobject,
                    testTotalScore=test_total_score
                )
            
        context={
            'status': 'success',
            'submitted':'false',
            'studentobject':studentobject.id,
            'test_set_group':test_set_group.id,
        }
        return JsonResponse(context, safe=False)
        
    context={
        'submitted':'true',
        'message':"your previous response have been taken, you can't submit twice"
    }
    return JsonResponse(context, safe=False)


def success_view(request,student_id,student_test_id):
    studentobject=Students_Pin_and_ID.objects.get(id=student_id)
    studenttestobject=TestSetGroup.objects.get(id=student_test_id)

    context={
        "studentobject":studentobject,
        "studenttestobject":studenttestobject,
    }
    return render(request,'success.html',context)


# Question Formulation CRUD
def get_questions_and_answers(request, questionset_id):
    try:
        question_set = QuestionSet.objects.get(id=questionset_id)
        questions = question_set.questions.all()
        data = []
        for question in questions:
            answers = question.answers.all()
            answerslist=[]
            for answer in answers:
                answerslist.append({
                    "id":answer.answerId,
                    "answerText":answer.answertext,
                    "isCorrect":answer.isCorrect
                })
            data.append({
                "id":question.questionId,
                "questionText": question.questiontext,
                "answers": answerslist,
                "questionMark": question.questionMark,
                "questionrequired": question.required,
            })
        return JsonResponse(data, safe=False)
    except QuestionSet.DoesNotExist:
        return JsonResponse({"message": "Question Set not found"}, status=404)


def save_question_to_questionset(request, questionset_id):
    data = json.loads(request.body)
    question_id = data['question_id']
    question_text = data['question_text']
    question_mark = data['question_mark']
    question_required = data['question_required']
    question,created = Question.objects.get_or_create(questionId=question_id,questiontext=question_text,questionMark=question_mark,required=question_required)
    question.save()
    for answer in data['question_answers']:
        answer,created = Answer.objects.get_or_create(
            answerId=answer['id'],
            answertext=answer['answerText'],
            isCorrect=answer['isCorrect']
        )
        answer.save()
        question.answers.add(answer)

    question_set = QuestionSet.objects.get(id=questionset_id)
    question_set.questions.add(question)
    return JsonResponse({"message": "Question added successfully"}, status=200)  

def update_question_to_questionset(request, questionset_id):
    data = json.loads(request.body)
    question_id = data['question_id']
    question_text = data['question_text']
    question_mark = data['question_mark']
    question_required = data['question_required']
    question_set = QuestionSet.objects.get(id=questionset_id)
    question = Question.objects.get(questionId=question_id)
    Answer.objects.filter(question=question).delete()
    question_set.questions.remove(question)
    question.questiontext = question_text
    question.questionMark = question_mark
    question.required = question_required
    question.save()
    for answer in data['question_answers']:
        answer = Answer.objects.create(
            answerId=answer['id'],
            answertext=answer['answerText'],
            isCorrect=answer['isCorrect']
        )
        answer.save()
        question.answers.add(answer)
    question_set.questions.add(question)
    return JsonResponse({"message": "Question update successfully"}, status=200)  


def remove_question_from_questionset(request, questionset_id):
    data = json.loads(request.body)
    question_id = data['question_id']
    question_set = QuestionSet.objects.get(id=questionset_id)
    question = Question.objects.get(id=question_id)
    Answer.objects.filter(question=question).delete()
    question_set.questions.remove(question)
    question.delete()
    return JsonResponse({"message": "Question removed successfully"}, status=200)

   

def remove_all_questions_from_questionset(request, questionset_id):
    try:
        question_set = QuestionSet.objects.get(id=questionset_id)
        questions = question_set.questions.all()
        question_set.questions.clear()
        for question in questions:
            Answer.objects.filter(question=question).delete()
            question.delete()
        return JsonResponse({"message": "All questions and associated answers removed successfully"}, status=200)
    except QuestionSet.DoesNotExist:
        return JsonResponse({"message": "Question Set not found"}, status=404)

   

