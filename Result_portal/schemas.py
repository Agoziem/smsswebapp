from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


# AcademicSession Schemas
class AcademicSessionBase(BaseModel):
    session: str = Field(..., max_length=100, description="Academic session")


class AcademicSessionCreateSchema(AcademicSessionBase):
    """Schema for creating a new academic session"""
    pass


class AcademicSessionUpdateSchema(BaseModel):
    """Schema for updating an academic session"""
    session: Optional[str] = Field(None, max_length=100, description="Academic session")


class AcademicSessionResponseSchema(AcademicSessionBase):
    """Schema for academic session response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class AcademicSessionDeleteSchema(BaseModel):
    """Schema for academic session deletion confirmation"""
    message: str = Field(default="Academic session deleted successfully")
    deleted_id: int


# Term Schemas
class TermBase(BaseModel):
    term: str = Field(..., max_length=100, description="Term")


class TermCreateSchema(TermBase):
    """Schema for creating a new term"""
    pass


class TermUpdateSchema(BaseModel):
    """Schema for updating a term"""
    term: Optional[str] = Field(None, max_length=100, description="Term")


class TermResponseSchema(TermBase):
    """Schema for term response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class TermDeleteSchema(BaseModel):
    """Schema for term deletion confirmation"""
    message: str = Field(default="Term deleted successfully")
    deleted_id: int


# Class Schemas
class ClassBase(BaseModel):
    class_name: str = Field(..., max_length=10, description="Class name")


class ClassCreateSchema(ClassBase):
    """Schema for creating a new class"""
    pass


class ClassUpdateSchema(BaseModel):
    """Schema for updating a class"""
    class_name: Optional[str] = Field(None, max_length=10, description="Class name")


class ClassResponseSchema(ClassBase):
    """Schema for class response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ClassDeleteSchema(BaseModel):
    """Schema for class deletion confirmation"""
    message: str = Field(default="Class deleted successfully")
    deleted_id: int


# Subject Schemas
class SubjectBase(BaseModel):
    subject_code: str = Field(..., max_length=100, description="Subject code")
    subject_name: str = Field(..., max_length=100, description="Subject name")


class SubjectCreateSchema(SubjectBase):
    """Schema for creating a new subject"""
    pass


class SubjectUpdateSchema(BaseModel):
    """Schema for updating a subject"""
    subject_code: Optional[str] = Field(None, max_length=100, description="Subject code")
    subject_name: Optional[str] = Field(None, max_length=100, description="Subject name")


class SubjectResponseSchema(SubjectBase):
    """Schema for subject response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class SubjectDeleteSchema(BaseModel):
    """Schema for subject deletion confirmation"""
    message: str = Field(default="Subject deleted successfully")
    deleted_id: int


# Subjectallocation Schemas
class SubjectallocationBase(BaseModel):
    pass


class SubjectallocationCreateSchema(SubjectallocationBase):
    """Schema for creating a new subject allocation"""
    classname_id: int = Field(..., description="Class ID")
    subject_ids: List[int] = Field(default_factory=list, description="List of subject IDs")


class SubjectallocationUpdateSchema(BaseModel):
    """Schema for updating a subject allocation"""
    classname_id: Optional[int] = Field(None, description="Class ID")
    subject_ids: Optional[List[int]] = Field(None, description="List of subject IDs")


class SubjectallocationResponseSchema(SubjectallocationBase):
    """Schema for subject allocation response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    class_name: Optional[str] = Field(None, description="Class name")
    subjects: List[SubjectResponseSchema] = Field(default_factory=list, description="List of subjects")


class SubjectallocationDeleteSchema(BaseModel):
    """Schema for subject allocation deletion confirmation"""
    message: str = Field(default="Subject allocation deleted successfully")
    deleted_id: int


# Newsletter Schemas
class NewsletterBase(BaseModel):
    newsletter: Optional[str] = Field(None, description="Newsletter content")


class NewsletterCreateSchema(NewsletterBase):
    """Schema for creating a new newsletter"""
    current_term_id: Optional[int] = Field(None, description="Current term ID")
    newsletter_file: Optional[str] = Field(None, description="Newsletter file")


class NewsletterUpdateSchema(BaseModel):
    """Schema for updating a newsletter"""
    current_term_id: Optional[int] = Field(None, description="Current term ID")
    newsletter: Optional[str] = Field(None, description="Newsletter content")
    newsletter_file: Optional[str] = Field(None, description="Newsletter file")


class NewsletterResponseSchema(NewsletterBase):
    """Schema for newsletter response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    current_term: Optional[str] = Field(None, description="Current term")
    newsletter_file_url: Optional[str] = Field(None, description="Newsletter file URL")


class NewsletterDeleteSchema(BaseModel):
    """Schema for newsletter deletion confirmation"""
    message: str = Field(default="Newsletter deleted successfully")
    deleted_id: int


# Assignments Schemas
class AssignmentsBase(BaseModel):
    subject: str = Field(..., max_length=200, description="Subject")


class AssignmentsCreateSchema(AssignmentsBase):
    """Schema for creating a new assignment"""
    class_id: Optional[int] = Field(None, description="Class ID")
    file: Optional[str] = Field(None, description="Assignment file")


class AssignmentsUpdateSchema(BaseModel):
    """Schema for updating an assignment"""
    class_id: Optional[int] = Field(None, description="Class ID")
    subject: Optional[str] = Field(None, max_length=200, description="Subject")
    file: Optional[str] = Field(None, description="Assignment file")


class AssignmentsResponseSchema(AssignmentsBase):
    """Schema for assignments response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    class_name: Optional[str] = Field(None, description="Class name")
    file_url: Optional[str] = Field(None, description="Assignment file URL")


class AssignmentsDeleteSchema(BaseModel):
    """Schema for assignments deletion confirmation"""
    message: str = Field(default="Assignment deleted successfully")
    deleted_id: int


# Students_Pin_and_ID Schemas
class StudentsBase(BaseModel):
    student_name: str = Field(default="No name", max_length=100, description="Student name")
    sex: Optional[str] = Field(None, max_length=100, description="Student sex")


class StudentsCreateSchema(StudentsBase):
    """Schema for creating a new student"""
    sn: Optional[str] = Field(None, max_length=100, description="Serial number")
    student_photo: Optional[str] = Field(None, description="Student photo")
    student_password: str = Field(default="No password", max_length=100, description="Student password")


class StudentsUpdateSchema(BaseModel):
    """Schema for updating a student"""
    sn: Optional[str] = Field(None, max_length=100, description="Serial number")
    student_photo: Optional[str] = Field(None, description="Student photo")
    student_name: Optional[str] = Field(None, max_length=100, description="Student name")
    sex: Optional[str] = Field(None, max_length=100, description="Student sex")
    student_password: Optional[str] = Field(None, max_length=100, description="Student password")


class StudentsResponseSchema(StudentsBase):
    """Schema for students response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    sn: Optional[str] = Field(None, description="Serial number")
    student_photo: Optional[str] = Field(None, description="Student photo URL")
    student_id: Optional[str] = Field(None, description="Student ID")
    student_pin: Optional[str] = Field(None, description="Student PIN")


class StudentsDeleteSchema(BaseModel):
    """Schema for students deletion confirmation"""
    message: str = Field(default="Student deleted successfully")
    deleted_id: int


# StudentClassEnrollment Schemas
class StudentClassEnrollmentBase(BaseModel):
    pass


class StudentClassEnrollmentCreateSchema(StudentClassEnrollmentBase):
    """Schema for creating a new student class enrollment"""
    student_id: int = Field(..., description="Student ID")
    student_class_id: int = Field(..., description="Student class ID")
    academic_session_id: int = Field(..., description="Academic session ID")


class StudentClassEnrollmentUpdateSchema(BaseModel):
    """Schema for updating a student class enrollment"""
    student_id: Optional[int] = Field(None, description="Student ID")
    student_class_id: Optional[int] = Field(None, description="Student class ID")
    academic_session_id: Optional[int] = Field(None, description="Academic session ID")


class StudentClassEnrollmentResponseSchema(StudentClassEnrollmentBase):
    """Schema for student class enrollment response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    class_name: Optional[str] = Field(None, description="Class name")
    academic_session: Optional[str] = Field(None, description="Academic session")


class StudentClassEnrollmentDeleteSchema(BaseModel):
    """Schema for student class enrollment deletion confirmation"""
    message: str = Field(default="Student class enrollment deleted successfully")
    deleted_id: int


# Student_Result_Data Schemas
class StudentResultDataBase(BaseModel):
    total_score: str = Field(default="-", max_length=100, description="Total score")
    total_number: str = Field(default="-", max_length=100, description="Total number")
    average: str = Field(default="-", max_length=100, description="Average")
    position: str = Field(default="-", max_length=100, description="Position")
    remark: str = Field(default="-", max_length=100, description="Remark")
    published: bool = Field(default=False, description="Published status")


class StudentResultDataCreateSchema(StudentResultDataBase):
    """Schema for creating new student result data"""
    student_name_id: int = Field(..., description="Student ID")
    term_id: Optional[int] = Field(None, description="Term ID")
    academic_session_id: Optional[int] = Field(None, description="Academic session ID")


class StudentResultDataUpdateSchema(BaseModel):
    """Schema for updating student result data"""
    student_name_id: Optional[int] = Field(None, description="Student ID")
    total_score: Optional[str] = Field(None, max_length=100, description="Total score")
    total_number: Optional[str] = Field(None, max_length=100, description="Total number")
    average: Optional[str] = Field(None, max_length=100, description="Average")
    position: Optional[str] = Field(None, max_length=100, description="Position")
    remark: Optional[str] = Field(None, max_length=100, description="Remark")
    term_id: Optional[int] = Field(None, description="Term ID")
    academic_session_id: Optional[int] = Field(None, description="Academic session ID")
    published: Optional[bool] = Field(None, description="Published status")


class StudentResultDataResponseSchema(StudentResultDataBase):
    """Schema for student result data response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    term: Optional[str] = Field(None, description="Term")
    academic_session: Optional[str] = Field(None, description="Academic session")


class StudentResultDataDeleteSchema(BaseModel):
    """Schema for student result data deletion confirmation"""
    message: str = Field(default="Student result data deleted successfully")
    deleted_id: int


# Result Schemas
class ResultBase(BaseModel):
    first_test: str = Field(default="-", max_length=100, description="First test score")
    first_ass: str = Field(default="-", max_length=100, description="First assignment score")
    mid_term_test: str = Field(default="-", max_length=100, description="Mid term test score")
    second_ass: str = Field(default="-", max_length=100, description="Second assignment score")
    second_test: str = Field(default="-", max_length=100, description="Second test score")
    ca: str = Field(default="-", max_length=100, description="Continuous assessment score")
    exam: str = Field(default="-", max_length=100, description="Exam score")
    total: str = Field(default="-", max_length=100, description="Total score")
    grade: str = Field(default="-", max_length=100, description="Grade")
    subject_position: str = Field(default="-", max_length=100, description="Subject position")
    remark: str = Field(default="-", max_length=100, description="Remark")
    published: bool = Field(default=False, description="Published status")


class ResultCreateSchema(ResultBase):
    """Schema for creating a new result"""
    student_id: int = Field(..., description="Student ID")
    student_class_id: Optional[int] = Field(None, description="Student class ID")
    students_result_summary_id: Optional[int] = Field(None, description="Students result summary ID")
    subject_id: int = Field(..., description="Subject ID")


class ResultUpdateSchema(BaseModel):
    """Schema for updating a result"""
    student_id: Optional[int] = Field(None, description="Student ID")
    student_class_id: Optional[int] = Field(None, description="Student class ID")
    students_result_summary_id: Optional[int] = Field(None, description="Students result summary ID")
    subject_id: Optional[int] = Field(None, description="Subject ID")
    first_test: Optional[str] = Field(None, max_length=100, description="First test score")
    first_ass: Optional[str] = Field(None, max_length=100, description="First assignment score")
    mid_term_test: Optional[str] = Field(None, max_length=100, description="Mid term test score")
    second_ass: Optional[str] = Field(None, max_length=100, description="Second assignment score")
    second_test: Optional[str] = Field(None, max_length=100, description="Second test score")
    ca: Optional[str] = Field(None, max_length=100, description="Continuous assessment score")
    exam: Optional[str] = Field(None, max_length=100, description="Exam score")
    total: Optional[str] = Field(None, max_length=100, description="Total score")
    grade: Optional[str] = Field(None, max_length=100, description="Grade")
    subject_position: Optional[str] = Field(None, max_length=100, description="Subject position")
    remark: Optional[str] = Field(None, max_length=100, description="Remark")
    published: Optional[bool] = Field(None, description="Published status")


class ResultResponseSchema(ResultBase):
    """Schema for result response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    student_class_name: Optional[str] = Field(None, description="Student class name")
    subject_name: Optional[str] = Field(None, description="Subject name")


class ResultDeleteSchema(BaseModel):
    """Schema for result deletion confirmation"""
    message: str = Field(default="Result deleted successfully")
    deleted_id: int


# AnnualStudent Schemas
class AnnualStudentBase(BaseModel):
    total_score: str = Field(default="-", max_length=100, description="Total score")
    total_number: str = Field(default="-", max_length=100, description="Total number")
    average: str = Field(default="-", max_length=100, description="Average")
    position: str = Field(default="-", max_length=100, description="Position")
    published: bool = Field(default=False, description="Published status")
    remark: str = Field(default="-", max_length=100, description="Remark")
    verdict: str = Field(default="-", max_length=100, description="Verdict")


class AnnualStudentCreateSchema(AnnualStudentBase):
    """Schema for creating a new annual student"""
    student_name_id: int = Field(..., description="Student ID")
    academic_session_id: Optional[int] = Field(None, description="Academic session ID")


class AnnualStudentUpdateSchema(BaseModel):
    """Schema for updating an annual student"""
    student_name_id: Optional[int] = Field(None, description="Student ID")
    total_score: Optional[str] = Field(None, max_length=100, description="Total score")
    total_number: Optional[str] = Field(None, max_length=100, description="Total number")
    average: Optional[str] = Field(None, max_length=100, description="Average")
    position: Optional[str] = Field(None, max_length=100, description="Position")
    academic_session_id: Optional[int] = Field(None, description="Academic session ID")
    published: Optional[bool] = Field(None, description="Published status")
    remark: Optional[str] = Field(None, max_length=100, description="Remark")
    verdict: Optional[str] = Field(None, max_length=100, description="Verdict")


class AnnualStudentResponseSchema(AnnualStudentBase):
    """Schema for annual student response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    academic_session: Optional[str] = Field(None, description="Academic session")


class AnnualStudentDeleteSchema(BaseModel):
    """Schema for annual student deletion confirmation"""
    message: str = Field(default="Annual student deleted successfully")
    deleted_id: int


# AnnualResult Schemas
class AnnualResultBase(BaseModel):
    first_term_total: str = Field(default="-", max_length=100, description="First term total")
    second_term_total: str = Field(default="-", max_length=100, description="Second term total")
    third_term_total: str = Field(default="-", max_length=100, description="Third term total")
    total: str = Field(default="-", max_length=100, description="Total")
    average: str = Field(default="-", max_length=100, description="Average")
    grade: str = Field(default="-", max_length=100, description="Grade")
    subject_position: str = Field(default="-", max_length=100, description="Subject position")
    remark: str = Field(default="-", max_length=100, description="Remark")
    published: bool = Field(default=False, description="Published status")


class AnnualResultCreateSchema(AnnualResultBase):
    """Schema for creating a new annual result"""
    student_name_id: int = Field(..., description="Annual student ID")
    subject_id: int = Field(..., description="Subject ID")


class AnnualResultUpdateSchema(BaseModel):
    """Schema for updating an annual result"""
    student_name_id: Optional[int] = Field(None, description="Annual student ID")
    subject_id: Optional[int] = Field(None, description="Subject ID")
    first_term_total: Optional[str] = Field(None, max_length=100, description="First term total")
    second_term_total: Optional[str] = Field(None, max_length=100, description="Second term total")
    third_term_total: Optional[str] = Field(None, max_length=100, description="Third term total")
    total: Optional[str] = Field(None, max_length=100, description="Total")
    average: Optional[str] = Field(None, max_length=100, description="Average")
    grade: Optional[str] = Field(None, max_length=100, description="Grade")
    subject_position: Optional[str] = Field(None, max_length=100, description="Subject position")
    remark: Optional[str] = Field(None, max_length=100, description="Remark")
    published: Optional[bool] = Field(None, description="Published status")


class AnnualResultResponseSchema(AnnualResultBase):
    """Schema for annual result response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    subject_name: Optional[str] = Field(None, description="Subject name")


class AnnualResultDeleteSchema(BaseModel):
    """Schema for annual result deletion confirmation"""
    message: str = Field(default="Annual result deleted successfully")
    deleted_id: int