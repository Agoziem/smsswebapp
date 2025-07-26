from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import QuestionSet, Question
from Result_portal.models import Class, Subject
from Teachers_Portal.models import Teacher
from ..schemas import (
    QuestionSetCreateSchema,
    QuestionSetUpdateSchema,
    QuestionSetResponseSchema,
    QuestionSetDeleteSchema,
    QuestionResponseSchema,
    AnswerResponseSchema
)

router = Router(tags=["Question Sets"])


@router.get("/", response=List[QuestionSetResponseSchema])
def list_question_sets(request):
    """Get all question sets"""
    question_sets = QuestionSet.objects.select_related('subject', 'teacher').prefetch_related('ExamClass', 'questions__answers').all()
    
    return [
        QuestionSetResponseSchema(
            id=qs.pk,
            exam_time=qs.examTime,
            subject_name=qs.subject.subject_name if qs.subject else None,
            teacher_name=f"{qs.teacher.FirstName} {qs.teacher.LastName}" if qs.teacher else None,
            exam_classes=[cls.Class for cls in qs.ExamClass.all()],
            questions=[
                QuestionResponseSchema(
                    id=q.pk,
                    question_id=q.questionId,
                    question_text=q.questiontext,
                    question_mark=q.questionMark,
                    required=q.required,
                    answers=[
                        AnswerResponseSchema(
                            id=a.pk,
                            answer_id=a.answerId,
                            answer_text=a.answertext,
                            is_correct=a.isCorrect
                        ) for a in q.answers.all()
                    ]
                ) for q in qs.questions.all()
            ]
        ) for qs in question_sets
    ]


@router.get("/{question_set_id}", response=QuestionSetResponseSchema)
def get_question_set(request, question_set_id: int):
    """Get a specific question set by ID"""
    qs = get_object_or_404(
        QuestionSet.objects.select_related('subject', 'teacher').prefetch_related('ExamClass', 'questions__answers'),
        id=question_set_id
    )
    
    return QuestionSetResponseSchema(
        id=qs.pk,
        exam_time=qs.examTime,
        subject_name=qs.subject.subject_name if qs.subject else None,
        teacher_name=f"{qs.teacher.FirstName} {qs.teacher.LastName}" if qs.teacher else None,
        exam_classes=[cls.Class for cls in qs.ExamClass.all()],
        questions=[
            QuestionResponseSchema(
                id=q.pk,
                question_id=q.questionId,
                question_text=q.questiontext,
                question_mark=q.questionMark,
                required=q.required,
                answers=[
                    AnswerResponseSchema(
                        id=a.id,
                        answer_id=a.answerId,
                        answer_text=a.answertext,
                        is_correct=a.isCorrect
                    ) for a in q.answers.all()
                ]
            ) for q in qs.questions.all()
        ]
    )


@router.post("/", response=QuestionSetResponseSchema)
def create_question_set(request, payload: QuestionSetCreateSchema):
    """Create a new question set"""
    # Get related objects
    subject = get_object_or_404(Subject, id=payload.subject_id)
    teacher = get_object_or_404(Teacher, id=payload.teacher_id)
    
    # Create question set
    question_set = QuestionSet.objects.create(
        subject=subject,
        teacher=teacher,
        examTime=payload.exam_time
    )
    
    # Add exam classes
    if payload.exam_class_ids:
        exam_classes = Class.objects.filter(id__in=payload.exam_class_ids)
        question_set.ExamClass.set(exam_classes)
    
    # Add questions
    if payload.question_ids:
        questions = Question.objects.filter(id__in=payload.question_ids)
        question_set.questions.set(questions)
    
    # Refresh from database to get related objects
    question_set.refresh_from_db()
    
    return QuestionSetResponseSchema(
        id=question_set.pk,
        exam_time=question_set.examTime,
        subject_name=question_set.subject.subject_name,
        teacher_name=f"{question_set.teacher.FirstName} {question_set.teacher.LastName}",
        exam_classes=[cls.Class for cls in question_set.ExamClass.all()],
        questions=[
            QuestionResponseSchema(
                id=q.pk,
                question_id=q.questionId,
                question_text=q.questiontext,
                question_mark=q.questionMark,
                required=q.required,
                answers=[
                    AnswerResponseSchema(
                        id=a.pk,
                        answer_id=a.answerId,
                        answer_text=a.answertext,
                        is_correct=a.isCorrect
                    ) for a in q.answers.all()
                ]
            ) for q in question_set.questions.all()
        ]
    )


@router.put("/{question_set_id}", response=QuestionSetResponseSchema)
def update_question_set(request, question_set_id: int, payload: QuestionSetUpdateSchema):
    """Update an existing question set"""
    question_set = get_object_or_404(QuestionSet, id=question_set_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    # Update basic fields
    if 'exam_time' in update_data:
        question_set.examTime = update_data['exam_time']
    
    # Update related objects
    if 'subject_id' in update_data:
        subject = get_object_or_404(Subject, id=update_data['subject_id'])
        question_set.subject = subject
    
    if 'teacher_id' in update_data:
        teacher = get_object_or_404(Teacher, id=update_data['teacher_id'])
        question_set.teacher = teacher
    
    question_set.save()
    
    # Update many-to-many relationships
    if 'exam_class_ids' in update_data:
        exam_classes = Class.objects.filter(id__in=update_data['exam_class_ids'])
        question_set.ExamClass.set(exam_classes)
    
    if 'question_ids' in update_data:
        questions = Question.objects.filter(id__in=update_data['question_ids'])
        question_set.questions.set(questions)
    
    # Refresh and return
    question_set.refresh_from_db()
    
    return QuestionSetResponseSchema(
        id=question_set.pk,
        exam_time=question_set.examTime,
        subject_name=question_set.subject.subject_name,
        teacher_name=f"{question_set.teacher.FirstName} {question_set.teacher.LastName}",
        exam_classes=[cls.Class for cls in question_set.ExamClass.all()],
        questions=[
            QuestionResponseSchema(
                id=q.pk,
                question_id=q.questionId,
                question_text=q.questiontext,
                question_mark=q.questionMark,
                required=q.required,
                answers=[
                    AnswerResponseSchema(
                        id=a.id,
                        answer_id=a.answerId,
                        answer_text=a.answertext,
                        is_correct=a.isCorrect
                    ) for a in q.answers.all()
                ]
            ) for q in question_set.questions.all()
        ]
    )


@router.delete("/{question_set_id}", response=QuestionSetDeleteSchema)
def delete_question_set(request, question_set_id: int):
    """Delete a question set"""
    question_set = get_object_or_404(QuestionSet, id=question_set_id)
    question_set.delete()
    return QuestionSetDeleteSchema(deleted_id=question_set_id)
