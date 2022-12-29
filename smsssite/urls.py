"""smsssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home2'),
    path('home/',home2_view, name='home'),
    path('submit_contact_form/', submit_contact_form, name='submit_contact_form' ),
    path('submit_sub_form/', submit_sub_form, name='submit_sub_form' ),
    path('Elibrary/', include('Elibrary.urls')),
    path('gallery/', photo_gallery_view, name='gallery'),
    # path('Blog/', include('Blog.urls')),
    path('Payment_portal/', include('Payment_portal.urls')),
    path('Result_portal/', include('Result_portal.urls')),
    # path('CBT/', include('CBT.urls')),
    path('Admission_form/', include('Admission_form.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='SMSS Omagba'
admin.site.index_title='Site Administration'