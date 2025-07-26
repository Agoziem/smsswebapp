from ninja import ModelSchema, Schema
from typing import Optional, List
from .models import (
    AcademicSession, Term, Class, Subject, Subjectallocation,
    Newsletter, Assignments, Excelfiles, StudentClassEnrollment,
    Students_Pin_and_ID, Student_Result_Data, Result, 
    AnnualStudent, AnnualResult
)


# Success Response Schema
class SuccessResponseSchema(Schema):
    message: str


# AcademicSession Schemas
class AcademicSessionCreateSchema(Schema):
    """Schema for creating a new academic session"""
    session: str


class AcademicSessionUpdateSchema(Schema):
    """Schema for updating an academic session"""
    session: Optional[str] = None


class AcademicSessionResponseSchema(ModelSchema):
    """Schema for academic session response"""
    class Meta:
        model = AcademicSession
        fields = '__all__'


# Term Schemas
class TermCreateSchema(Schema):
    """Schema for creating a new term"""
    term: str


class TermUpdateSchema(Schema):
    """Schema for updating a term"""
    term: Optional[str] = None


class TermResponseSchema(ModelSchema):
    """Schema for term response"""
    class Meta:
        model = Term
        fields = '__all__'


# Class Schemas
class ClassCreateSchema(Schema):
    """Schema for creating a new class"""
    Class: str


class ClassUpdateSchema(Schema):
    """Schema for updating a class"""
    Class: Optional[str] = None


class ClassResponseSchema(ModelSchema):
    """Schema for class response"""
    class Meta:
        model = Class
        fields = '__all__'


# Subject Schemas
class SubjectCreateSchema(Schema):
    """Schema for creating a new subject"""
    subject_code: str
    subject_name: str


class SubjectUpdateSchema(Schema):
    """Schema for updating a subject"""
    subject_code: Optional[str] = None
    subject_name: Optional[str] = None


class SubjectResponseSchema(ModelSchema):
    """Schema for subject response"""
    class Meta:
        model = Subject
        fields = '__all__'


# Subjectallocation Schemas
class SubjectallocationCreateSchema(Schema):
    """Schema for creating a new subject allocation"""
    classname_id: int
    subject_ids: List[int]


class SubjectallocationUpdateSchema(Schema):
    """Schema for updating a subject allocation"""
    classname_id: Optional[int] = None
    subject_ids: Optional[List[int]] = None


class SubjectallocationResponseSchema(ModelSchema):
    """Schema for subject allocation response"""
    class Meta:
        model = Subjectallocation
        fields = '__all__'


# Newsletter Schemas
class NewsletterCreateSchema(Schema):
    """Schema for creating a new newsletter"""
    currentTerm_id: Optional[int] = None
    newsletter: Optional[str] = None
    newsletterFile: Optional[str] = None


class NewsletterUpdateSchema(Schema):
    """Schema for updating a newsletter"""
    currentTerm_id: Optional[int] = None
    newsletter: Optional[str] = None
    newsletterFile: Optional[str] = None


class NewsletterResponseSchema(ModelSchema):
    """Schema for newsletter response"""
    class Meta:
        model = Newsletter
        fields = '__all__'


# Assignments Schemas
class AssignmentsCreateSchema(Schema):
    """Schema for creating a new assignment"""
    Class_id: Optional[int] = None
    subject: str
    file: Optional[str] = None


class AssignmentsUpdateSchema(Schema):
    """Schema for updating an assignment"""
    Class_id: Optional[int] = None
    subject: Optional[str] = None
    file: Optional[str] = None


class AssignmentsResponseSchema(ModelSchema):
    """Schema for assignments response"""
    class Meta:
        model = Assignments
        fields = '__all__'


# Excelfiles Schemas
class ExcelfilesCreateSchema(Schema):
    """Schema for creating a new excel file"""
    Excel: Optional[str] = None


class ExcelfilesUpdateSchema(Schema):
    """Schema for updating an excel file"""
    Excel: Optional[str] = None


class ExcelfilesResponseSchema(ModelSchema):
    """Schema for excel files response"""
    class Meta:
        model = Excelfiles
        fields = '__all__'


# StudentClassEnrollment Schemas
class StudentClassEnrollmentCreateSchema(Schema):
    """Schema for creating a new student class enrollment"""
    student_id: int
    student_class_id: int
    academic_session_id: int


class StudentClassEnrollmentUpdateSchema(Schema):
    """Schema for updating a student class enrollment"""
    student_id: Optional[int] = None
    student_class_id: Optional[int] = None
    academic_session_id: Optional[int] = None


class StudentClassEnrollmentResponseSchema(ModelSchema):
    """Schema for student class enrollment response"""
    class Meta:
        model = StudentClassEnrollment
        fields = '__all__'


# Students_Pin_and_ID Schemas
class StudentsPinAndIDCreateSchema(Schema):
    """Schema for creating a new student"""
    SN: Optional[str] = None
    student_Photo: Optional[str] = None
    student_name: str
    Sex: Optional[str] = None
    student_pin: Optional[str] = None
    student_password: Optional[str] = None


class StudentsPinAndIDUpdateSchema(Schema):
    """Schema for updating a student"""
    SN: Optional[str] = None
    student_Photo: Optional[str] = None
    student_name: Optional[str] = None
    Sex: Optional[str] = None
    student_pin: Optional[str] = None
    student_password: Optional[str] = None


class StudentsPinAndIDResponseSchema(ModelSchema):
    """Schema for students pin and ID response"""
    class Meta:
        model = Students_Pin_and_ID
        fields = '__all__'


# Student_Result_Data Schemas
class StudentResultDataCreateSchema(Schema):
    """Schema for creating a new student result data"""
    student_name_id: int
    TotalScore: Optional[str] = None
    Totalnumber: Optional[str] = None
    Average: Optional[str] = None
    Position: Optional[str] = None
    Remark: Optional[str] = None
    Term_id: Optional[int] = None
    AcademicSession_id: Optional[int] = None
    published: bool = False


class StudentResultDataUpdateSchema(Schema):
    """Schema for updating a student result data"""
    student_name_id: Optional[int] = None
    TotalScore: Optional[str] = None
    Totalnumber: Optional[str] = None
    Average: Optional[str] = None
    Position: Optional[str] = None
    Remark: Optional[str] = None
    Term_id: Optional[int] = None
    AcademicSession_id: Optional[int] = None
    published: Optional[bool] = None


class StudentResultDataResponseSchema(ModelSchema):
    """Schema for student result data response"""
    class Meta:
        model = Student_Result_Data
        fields = '__all__'


# Result Schemas
class ResultCreateSchema(Schema):
    """Schema for creating a new result"""
    student_id: int
    student_class_id: Optional[int] = None
    students_result_summary_id: Optional[int] = None
    Subject_id: int
    FirstTest: Optional[str] = None
    FirstAss: Optional[str] = None
    MidTermTest: Optional[str] = None
    SecondAss: Optional[str] = None
    SecondTest: Optional[str] = None
    CA: Optional[str] = None
    Exam: Optional[str] = None
    Total: Optional[str] = None
    Grade: Optional[str] = None
    SubjectPosition: Optional[str] = None
    Remark: Optional[str] = None
    published: bool = False


class ResultUpdateSchema(Schema):
    """Schema for updating a result"""
    student_id: Optional[int] = None
    student_class_id: Optional[int] = None
    students_result_summary_id: Optional[int] = None
    Subject_id: Optional[int] = None
    FirstTest: Optional[str] = None
    FirstAss: Optional[str] = None
    MidTermTest: Optional[str] = None
    SecondAss: Optional[str] = None
    SecondTest: Optional[str] = None
    CA: Optional[str] = None
    Exam: Optional[str] = None
    Total: Optional[str] = None
    Grade: Optional[str] = None
    SubjectPosition: Optional[str] = None
    Remark: Optional[str] = None
    published: Optional[bool] = None


class ResultResponseSchema(ModelSchema):
    """Schema for result response"""
    class Meta:
        model = Result
        fields = '__all__'


# AnnualStudent Schemas
class AnnualStudentCreateSchema(Schema):
    """Schema for creating a new annual student"""
    student_name_id: int
    TotalScore: Optional[str] = None
    Totalnumber: Optional[str] = None
    Average: Optional[str] = None
    Position: Optional[str] = None
    academicsession_id: Optional[int] = None
    published: bool = False
    Remark: Optional[str] = None
    Verdict: Optional[str] = None


class AnnualStudentUpdateSchema(Schema):
    """Schema for updating an annual student"""
    student_name_id: Optional[int] = None
    TotalScore: Optional[str] = None
    Totalnumber: Optional[str] = None
    Average: Optional[str] = None
    Position: Optional[str] = None
    academicsession_id: Optional[int] = None
    published: Optional[bool] = None
    Remark: Optional[str] = None
    Verdict: Optional[str] = None


class AnnualStudentResponseSchema(ModelSchema):
    """Schema for annual student response"""
    class Meta:
        model = AnnualStudent
        fields = '__all__'


# AnnualResult Schemas
class AnnualResultCreateSchema(Schema):
    """Schema for creating a new annual result"""
    student_name_id: int
    Subject_id: int
    FirstTermTotal: Optional[str] = None
    SecondTermTotal: Optional[str] = None
    ThirdTermTotal: Optional[str] = None
    Total: Optional[str] = None
    Average: Optional[str] = None
    Grade: Optional[str] = None
    SubjectPosition: Optional[str] = None
    Remark: Optional[str] = None
    published: bool = False


class AnnualResultUpdateSchema(Schema):
    """Schema for updating an annual result"""
    student_name_id: Optional[int] = None
    Subject_id: Optional[int] = None
    FirstTermTotal: Optional[str] = None
    SecondTermTotal: Optional[str] = None
    ThirdTermTotal: Optional[str] = None
    Total: Optional[str] = None
    Average: Optional[str] = None
    Grade: Optional[str] = None
    SubjectPosition: Optional[str] = None
    Remark: Optional[str] = None
    published: Optional[bool] = None


class AnnualResultResponseSchema(ModelSchema):
    """Schema for annual result response"""
    class Meta:
        model = AnnualResult
        fields = '__all__'
