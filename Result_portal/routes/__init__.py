from .academic import academic_session_router, term_router, class_router, subject_router
from .students import students_router, enrollment_router
from .results import student_result_data_router, result_router, annual_student_router, annual_result_router

__all__ = [
    "academic_session_router",
    "term_router", 
    "class_router", 
    "subject_router",
    "students_router", 
    "enrollment_router",
    "student_result_data_router", 
    "result_router", 
    "annual_student_router", 
    "annual_result_router"
]
