from django.urls import path
from .views.views import *
from .views.Cbtviews import *
from .views.attendanceviews import *
from .views.adminviews import *
from .views.formteachersviews import *
from .views.classteachersviews import *

# 
app_name = 'Teachers_portal'
urlpatterns = [
    # Teachers Portal URLS
	path('',Teachers_dashboard_view , name='Teachers_dashboard'),
	path('<int:id>/profile/', profile_view , name='profile'),
	
	# CBT Portal URLS
	path('<int:teachers_id>/CBT_questions/',CBT_Questions_view , name='CBT_Questions'),
	path('<int:id>/CBT_update_details/',CBT_update_details , name='CBT_update_details'),
	path('submit_questions/',submitquestion_view , name='Submit_questions'),

    # Form Teachers Portal URLS
	path('<str:Classname>/PublishResults/',PublishResults_view , name='PublishResults'),   
	path('getstudentsubjecttotals/',getstudentsubjecttotals_view , name='getstudentsubjecttotals'),   
	path('publishstudentresult/',publish_student_result_view , name='publishstudentresult'),
    path('unpublishclassresult/',unpublish_classresults_view , name='unpublishstudentresult'),
    path('<str:Classname>/AnnualResults/',PublishAnnualResults_view , name='AnnualResults'), 
    path('annualclassresultcomputation/',annual_class_computation_view , name='annualclassresultcomputation'),
    path('publishannualclassresult/',publish_annualstudentresult_view , name='publishannualresult'),
    path('unpublishannualclassresult/',unpublish_annual_classresults_view , name='unpublishannualresult'),

	path('<str:Classname>/Students/',Students_view , name='Students'),   
	path('newStudent/', createstudent_view , name='createstudent'),   
	path('updateStudent/', updatestudent_view , name='updatestudent'),   
	path('DeleteStudents/', DeleteStudents_view , name='DeleteStudents'),   
	path('<str:Classname>/attendance',attendance_view, name='mark_attendance'),
    path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    
	# Class Teachers Portal URLS
	path('<str:Classname>/<int:id>/result_computation/',result_computation_view , name='result_computation'),
	path('getstudentresults/',get_students_result_view , name='getstudentresults'),   
	path('updatestudentresults/',update_student_result_view , name='updatestudentresults'),   
	path('submitallstudentresult/',submitallstudentresult_view , name='submitallstudentresult'),
    path('unpublishstudentresults/',unpublish_results_view , name='unpublishstudentresults'),
    path('<str:Classname>/<int:id>/annualresult_computation/',annualresult_computation , name='annualresult_computation'),
    path('annualresultcomputation/',annual_result_computation_view , name='annualresultcomputation'),
    path('publishannualresults/',publish_annual_results , name='publishannualresults'),
    path('unpublishannualresults/',unpublish_annual_results , name='unpublishannualresults'),
    
	# Admin urls
    path('schoolresults/',schoolresult_view , name='schoolresults'),
    path('getclasspublishedResults/',getclasspublishedResults , name='getclasspublishedResults'),
	path('schoolannualresult/',schoolannualresult_view, name='schoolannualresult'),
    path('getclassannualpublishedResults/',getclassannualpublishedResults, name='getclassannualpublishedResults'),
]