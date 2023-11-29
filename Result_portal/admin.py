from django.contrib import admin
from.models import *


admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(Subjectallocation)
admin.site.register(Excelfiles)
admin.site.register(Newsletter)
admin.site.register(Assignments)
admin.site.register(AnnualStudent)
admin.site.register(AnnualResult)

@admin.register(Students_Pin_and_ID)
class Students_Pin_and_IDAdmin(admin.ModelAdmin):
    list_display=('student_name','student_id','student_class')
    ordering=('student_name','student_class')
    search_fields=('student_name','student_class')
    list_filter=('student_class',"student_name")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subject_name','subject_code')
    ordering=('subject_name','subject_code')
    search_fields=('subject_name','subject_code')
    list_filter=('subject_name','subject_code')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=('Class',)
    ordering=('Class',)
    search_fields=('Class',)
    list_filter=('Class',)

@admin.register(Student_Result_Data)
class Student_Result_DataAdmin(admin.ModelAdmin):
    list_display=('Student_name','Position','display_Class','Average','Term')
    ordering=('Student_name','Position','Average','Term')
    search_fields=('Position','Average','Term')
    list_filter=('Student_name','Position','Average','Term')

    def display_Class(self, obj):
        return obj.Student_name.student_class

    display_Class.short_description = 'Class'

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','student_class','Subject')
    ordering = ('student','student_class','Subject')
    search_fields = ('student_class','Subject') 
    list_filter = ('student','student_class','Subject')


# @admin.register(AnnualStudent)
# class AnnualStudentAdmin(admin.ModelAdmin):
#     list_display=('Student_name','TotalScore','Average','Position')
#     ordering=('Student_name','TotalScore','Average','Position')
#     search_fields=('TotalScore','Average','Position')
#     list_filter=('Student_name','TotalScore','Average','Position')

# @admin.register(AnnualResult)
# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('students_result_data__Student_name','Subject')
#     ordering = ('students_result_data__Student_name','Subject')
#     search_fields = ('students_result_data__Student_name','Subject') 
#     list_filter = ('students_result_data__Student_name','Subject')

