from django.contrib import admin
from .models import *

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)


@admin.register(QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('subject', 'display_classes')
    ordering = ('subject',)
    search_fields = ('subject',) 
    list_filter = ('subject',)

    def display_classes(self, obj):
        return ", ".join([str(cls) for cls in obj.ExamClass.all()])

    display_classes.short_description = 'Classes'

@admin.register(QuestionSetGroup)
class QuestionSetGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    ordering = ('name','date')
    search_fields = ('name','date') 
    list_filter = ('name','date')

@admin.register(TestSetGroup)
class TestSetGroupAdmin(admin.ModelAdmin):
    list_display = ('student', 'testClass',"name")
    ordering = ('student', 'testClass',"name")
    search_fields = ('student', 'testClass',"name") 
    list_filter = ('student', 'testClass',"name")

@admin.register(TestQuestionSet)
class TestQuestionSetAdmin(admin.ModelAdmin):
    list_display = ('testSubject', 'display_student', 'testSetGroup', 'testTotalScore')
    ordering = ('testSubject', 'testSetGroup', 'testTotalScore')
    search_fields = ('testSubject', 'testSetGroup')
    list_filter = ('testSubject', 'testSetGroup__student', 'testSetGroup__testClass', 'testSetGroup__name')

    def display_student(self, obj):
        return obj.testSetGroup.student

    display_student.short_description = 'Student'
