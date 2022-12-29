from django.contrib import admin
from .models import *


@admin.register(NewStudent)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('firstName','lastName','class_applying_for')
    ordering=('firstName','lastName',)
    search_fields=('firstName','lastName','class_applying_for')
    list_filter=('class_applying_for',)