from django.contrib import admin
from.models import Subject,Ebook

# admin.site.register(Subject)
#admin.site.register(Ebook)

@admin.register(Subject)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('Sub',)
    search_fields=('Sub',)

@admin.register(Ebook)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('EbookTitle','Ebookcategory','Ebookauthor','date_uploaded')
    ordering=('EbookTitle','date_uploaded')
    search_fields=('EbookTitle','Ebookcategory','Ebookauthor')
    list_filter=('Ebookcategory',)
