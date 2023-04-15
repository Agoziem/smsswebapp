from django.contrib import admin
from.models import Payment,Amount

# admin.site.register(Payment)
admin.site.register(Amount)

@admin.register(Payment)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('Name_of_student','verified','date_created')
    ordering=('Name_of_student',)
    search_fields=('Name_of_student','Payment_type')
    list_filter=('Payment_type','verified','date_created')