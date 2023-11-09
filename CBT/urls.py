from django.urls import path
from .views import *

app_name = 'CBT'
urlpatterns = [
    path('', CBT_view , name='Cbt'),
    path('Test/<int:student_id>/<int:class_id>/<int:questionGroup_id>/', test_view , name='Test'),
    path('submit_test/', submit_test_view , name='submit_test'),
    path('<int:student_id>/<int:student_test_id>/success/', success_view , name='success'),
    path('get-questions-answers/<int:questionset_id>/', get_questions_and_answers , name='get_questions_and_answers'),
    path('save-question/<int:questionset_id>/', save_question_to_questionset , name='save_question_to_questionset'),
    path('update-question/<int:questionset_id>/', update_question_to_questionset , name='update_question_to_questionset'),
    path('remove-question/<int:questionset_id>/', remove_question_from_questionset , name='remove_question_from_questionset'),
    path('remove-all-questions/<int:questionset_id>/', remove_all_questions_from_questionset , name='remove_all_questions_from_questionset'),
    
    ]