from django.contrib import admin
from django.urls import path,include
from Home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),

    # ///////////////////////////////// Result Activation
    path('activation/', activation_view, name='activation_side'),
    path('testallocation/', testallocation_view, name='testallocation'),
    path('activate/',student_card_view, name='cardactivate'),
    
    # ///////////////////////////////// Result Activation
    path('submit_contact_form/', submit_contact_form, name='submit_contact_form' ),
    path('submit_sub_form/', submit_sub_form, name='submit_sub_form' ),
    path('gallery/', photo_gallery_view, name='gallery'),
    path('Accounts/', include('Accounts.urls')),
    path('Result_portal/', include('Result_portal.urls')),
    path('Teachers_Portal/', include('Teachers_Portal.urls')),
    path('CBT/', include('CBT.urls')),
]

if settings.DEBUG_ENV:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("ckeditor5/", include('django_ckeditor_5.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header='SMSS Omagba'
admin.site.index_title='Site Administration'