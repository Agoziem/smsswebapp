from django.urls import path
from .views import *

app_name = 'Teachers_portal'
urlpatterns = [
	path('',Teachers_dashboard_view , name='Teachers_dashboard'),
	path('<int:id>/profile/', profile_view , name='profile'),
    
	path('<str:Classname>/result_computation/',result_computation_view , name='result_computation'),
	path('<int:teachers_id>/CBT_questions/',CBT_Questions_view , name='CBT_Questions'),
	path('<int:id>/CBT_update_details/',CBT_update_details , name='CBT_update_details'),
	path('submit_questions/',submitquestion_view , name='Submit_questions'),
	path('CBT_results/',CBT_result_view , name='CBT_Results'),
    
	path('<str:Classname>/Students/',Students_view , name='Students'),   
	path('newStudent/', createstudent_view , name='createstudent'),   
	path('updateStudent/', updatestudent_view , name='updatestudent'),   
	path('DeleteStudents/', DeleteStudents_view , name='DeleteStudents'),   
	path('<str:Classname>/attendance',attendance_view, name='mark_attendance'),
    path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    ]