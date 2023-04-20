from django.urls import path
from django.conf.urls import url
from .views import *
app_name = 'Result_portal'
urlpatterns = [
# Result Portal main Url
    path('', Result_Portal_view, name='classes'),
    path('<str:Classname>/', get_Students, name='get_students'),
    

# Termly Result Activation Urls ///////////////////////////////////////////////////
# Details ///////////////////////////////////////////
    # Jss1 Details 
    path('activation/createjuniorstudents1/', createjuniorstudent1_view, name='juniorstudents1'),
    # Jss2 Details
    path('activation/createjuniorstudents2/', createjuniorstudent2_view, name='juniorstudents2'),
    # Jss3 Details
    path('activation/createjuniorstudents3/', createjuniorstudent3_view, name='juniorstudents3'),

#  Results ///////////////////////////////////////////

    # JSS1 Result
    path('activation/createjuniorresults1/', createjuniorresult1_view, name='juniorresult1'),
    # JSS2 Result
    path('activation/createjuniorresults2/', createjuniorresult2_view, name='juniorresult2'),
    # JSS3 Result
    path('activation/createjuniorresults3/', createjuniorresult3_view, name='juniorresult3'),

# Details ///////////////////////////////////////////

    # Ss1 Details
    path('activation/createseniorstudents1/', createseniorstudent1_view, name='seniorstudents1'),
    # Ss2 Details
    path('activation/createseniorstudents2/', createseniorstudent2_view, name='seniorstudents2'),
    # Ss3 Details
    path('activation/createseniorstudents3/', createseniorstudent3_view, name='seniorstudents3'),


#  Results ///////////////////////////////////////////

    # SS1 Result
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),
    # SS2 Result  
    path('activation/createseniorresults2/', createseniorresult2_view, name='seniorresult2'),
    # SS3 Result  
    path('activation/createseniorresults3/', createseniorresult3_view, name='seniorresult3'),


# Annual Result Activation Urls ///////////////////////////////////////////////

# Details ///////////////////////////////////////////

    # Jss1 Details
    path('activation/createjuniorstudentsAnnual1/', createjuniorstudentAnnual1_view, name='juniorstudentsannual1'),
    # Jss2 Details
    path('activation/createjuniorstudentsAnnual2/', createjuniorstudentAnnual2_view, name='juniorstudentsannual2'),
    # Jss3 Details
    path('activation/createjuniorstudentsAnnual3/', createjuniorstudentAnnual3_view, name='juniorstudentsannual3'),
    
#  Results ///////////////////////////////////////////

    # JSS1 Result
    path('activation/createjuniorAnnualresults1/', createjuniorresultAnnual1_view, name='juniorresultannual1'),
    # JSS2 Result
    path('activation/createjuniorAnnualresults2/', createjuniorresultAnnual2_view, name='juniorresultannual2'),
    # JSS3 Result
    path('activation/createjuniorAnnualresults3/', createjuniorresultAnnual3_view, name='juniorresultannual3'),
    
# Details ///////////////////////////////////////////
    # Ss1 Details
    path('activation/createseniorAnnualstudents1/', createseniorstudentAnnual1_view, name='seniorstudentsannual1'),
    # Ss2 Details
    path('activation/createseniorAnnualstudents2/', createseniorstudentAnnual2_view, name='seniorstudentsannual2'),
    # Ss3 Details
    path('activation/createseniorAnnualstudents3/', createseniorstudentAnnual3_view, name='seniorstudentsannual3'),
   
#  Results ///////////////////////////////////////////
    # SS1 Result
    path('activation/createseniorAnnualresults1/', createseniorresultAnnual1_view, name='seniorresultannual1'),
    # SS2 Result  
    path('activation/createseniorAnnualresults2/', createseniorresultAnnual2_view, name='seniorresultannual2'),
    # SS3 Result 
    path('activation/createseniorAnnualresults3/', createseniorresultAnnual3_view, name='seniorresultannual3'),
    
]