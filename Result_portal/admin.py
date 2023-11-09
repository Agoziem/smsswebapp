from django.contrib import admin
from.models import *


admin.site.register(Result)
admin.site.register(AnnualResult)
admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(Excelfiles)
admin.site.register(Newsletter)
admin.site.register(Assignments)

@admin.register(Students_Pin_and_ID)
class Students_Pin_and_IDAdmin(admin.ModelAdmin):
    list_display=('student_name','student_id','student_class')
    ordering=('student_name','student_class')
    search_fields=('student_name','student_class')
    list_filter=('student_class',"student_name")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subject_name',)
    ordering=('subject_name',)
    search_fields=('subject_name',)
    list_filter=('subject_name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=('Class',)
    ordering=('Class',)
    search_fields=('Class',)
    list_filter=('Class',)

@admin.register(Student_Result_Data)
class Student_Result_DataAdmin(admin.ModelAdmin):
    list_display=('Student_name','Position','Average')
    ordering=('Student_name','Position','Average')
    search_fields=('Student_name','Position','Average')
    list_filter=('Student_name','Position','Average')

@admin.register(AnnualStudent)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('Student_name','TotalScore','Average','Position')
    ordering=('Student_name','TotalScore','Average','Position')
    search_fields=('Student_name','TotalScore','Average','Position')
    list_filter=('Student_name','TotalScore','Average','Position')

