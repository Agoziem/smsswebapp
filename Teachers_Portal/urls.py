from django.urls import path
from .views import *

app_name = 'Teachers_portal'
urlpatterns = [
	path('',Teachers_dashboard_view , name='Teachers_dashboard'),
	path('<int:id>/profile/', profile_view , name='profile'),
    
	
	path('<int:teachers_id>/CBT_questions/',CBT_Questions_view , name='CBT_Questions'),
	path('<int:id>/CBT_update_details/',CBT_update_details , name='CBT_update_details'),
	path('submit_questions/',submitquestion_view , name='Submit_questions'),

    
	path('<str:Classname>/Students/',Students_view , name='Students'),   
	path('<str:Classname>/PublishResults/',PublishResults_view , name='PublishResults'),   
	path('getstudentsubjecttotals/',getstudentsubjecttotals_view , name='getstudentsubjecttotals'),   
	path('publishstudentresult/',publishstudentresult_view , name='publishstudentresult'),   
	path('newStudent/', createstudent_view , name='createstudent'),   
	path('updateStudent/', updatestudent_view , name='updatestudent'),   
	path('DeleteStudents/', DeleteStudents_view , name='DeleteStudents'),   
	path('<str:Classname>/attendance',attendance_view, name='mark_attendance'),
    path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    
	path('<str:Classname>/<int:id>/result_computation/',result_computation_view , name='result_computation'),
	path('getstudentresults/',get_students_result_view , name='getstudentresults'),   
	path('updatestudentresults/',update_student_result_view , name='updatestudentresults'),   
	path('submitallstudentresult/',submitallstudentresult_view , name='submitallstudentresult'),   
]