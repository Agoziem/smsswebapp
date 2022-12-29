from django.contrib import admin
from.models import *

# admin.site.register(Student)
# admin.site.register(Class)
# admin.site.register(Result)
admin.site.register(Excelfiles)
admin.site.register(Newsletter)
# admin.site.register(Pin)
# admin.site.register(Assignments)


@admin.register(Students_Pin_and_ID)
class Students_Pin_and_IDAdmin(admin.ModelAdmin):
    list_display=('student_pin','student_name','student_id')
    search_fields=('student_pin','student_name','student_class')
    list_filter=('student_name','student_class')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('Name','Class','Position')
    ordering=('Name',)
    search_fields=('Name','Class','Position')
    list_filter=('Class','Position')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=('Name','Class','Subject')
    ordering=('Name',)
    search_fields=('Name','Class','Subject')
    list_filter=('Class','Subject')

@admin.register(AnnualStudent)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('Name','Class','Position')
    ordering=('Name',)
    search_fields=('Name','Class','Position')
    list_filter=('Class','Position')

@admin.register(AnnualResult)
class AnnualResult(admin.ModelAdmin):
    list_display=('Name','Class','Subject')
    ordering=('Name',)
    search_fields=('Name','Class','Subject')
    list_filter=('Class','Subject')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    search_fields=('Class',)
    ordering=('Class',)

@admin.register(Assignments)
class AssignmentsAdmin(admin.ModelAdmin):
    search_fields=('Class','subject')
    ordering=('Class',)
    list_filter=('Class','subject')

