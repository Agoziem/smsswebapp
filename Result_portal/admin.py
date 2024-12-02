from django.contrib import admin
from.models import *


admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(Subjectallocation)
admin.site.register(Excelfiles)
admin.site.register(Newsletter)
admin.site.register(Assignments)

@admin.register(Students_Pin_and_ID)
class Students_Pin_and_IDAdmin(admin.ModelAdmin):
    list_display=('student_name','student_id')
    ordering=('student_name','student_id')
    search_fields=('student_name','student_id')
    list_filter=("student_name",'student_id')

@admin.register(StudentClassEnrollment)
class StudentClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_student_class', 'get_academic_session')
    ordering = ('student__student_name', 'student_class__Class', 'academic_session__session')
    search_fields = ('student__student_name', 'student_class__Class', 'academic_session__session')
    list_filter = ('student_class', 'academic_session')

    # Custom method to display student name
    def get_student_name(self, obj):
        return obj.student.student_name
    get_student_name.short_description = "Student Name"

    # Custom method to display class name
    def get_student_class(self, obj):
        return obj.student_class.Class
    get_student_class.short_description = "Class"

    # Custom method to display academic session
    def get_academic_session(self, obj):
        return obj.academic_session.session
    get_academic_session.short_description = "Academic Session"



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
    list_display = ('Student_name', 'Position', 'Average')
    ordering = ('Student_name', 'Position', 'Average')
    search_fields = ('Position', 'Average')
    list_filter = ('Student_name', 'Position', 'Average')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','student_class','Subject')
    ordering = ('student','student_class','Subject')
    search_fields = ('student_class','Subject') 
    list_filter = ('student','student_class','Subject')

@admin.register(AnnualStudent)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display = ('Student_name', 'TotalScore', 'Average', 'Position')
    ordering = ('Student_name', 'TotalScore', 'Average', 'Position')
    search_fields = ('TotalScore', 'Average', 'Position')
    list_filter = ('Student_name', 'TotalScore', 'Average', 'Position')

@admin.register(AnnualResult)
class AnnualResultAdmin(admin.ModelAdmin):
    list_display = ('Student_name', 'Subject')
    ordering = ('Student_name', 'Subject')
    search_fields = ('Student_name', 'Subject__subject_name')
    list_filter = ('Student_name', 'Subject__subject_name')

