from django.contrib import admin
from .models import *

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionSet)
admin.site.register(ExamClass)
admin.site.register(ExamQuestion)
admin.site.register(ExamAnswer)
admin.site.register(StudentExam)
admin.site.register(Exam)
admin.site.register(CBTQuestions)

