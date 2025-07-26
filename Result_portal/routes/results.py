from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import (
    Student_Result_Data, Result, AnnualStudent, AnnualResult,
    Students_Pin_and_ID, Class, Subject, Term, AcademicSession
)
from ..schemas import (
    StudentResultDataCreateSchema,
    StudentResultDataUpdateSchema,
    StudentResultDataResponseSchema,
    StudentResultDataDeleteSchema,
    ResultCreateSchema,
    ResultUpdateSchema,
    ResultResponseSchema,
    ResultDeleteSchema,
    AnnualStudentCreateSchema,
    AnnualStudentUpdateSchema,
    AnnualStudentResponseSchema,
    AnnualStudentDeleteSchema,
    AnnualResultCreateSchema,
    AnnualResultUpdateSchema,
    AnnualResultResponseSchema,
    AnnualResultDeleteSchema
)

student_result_data_router = Router(tags=["Student Result Data"])
result_router = Router(tags=["Results"])
annual_student_router = Router(tags=["Annual Students"])
annual_result_router = Router(tags=["Annual Results"])


# Student Result Data routes
@student_result_data_router.get("/", response=List[StudentResultDataResponseSchema])
def list_student_result_data(request):
    """Get all student result data"""
    result_data = Student_Result_Data.objects.select_related('Student_name', 'Term', 'AcademicSession').all()
    return [
        StudentResultDataResponseSchema(
            id=data.pk,
            total_score=data.TotalScore if data.TotalScore is not None else "-",
            total_number=data.Totalnumber if data.Totalnumber is not None else "-",
            average=data.Average if data.Average is not None else "-",
            position=data.Position if data.Position is not None else "-",
            remark=data.Remark if data.Remark is not None else "-",
            published=data.published,
            student_name=data.Student_name.student_name if data.Student_name else None,
            term=data.Term.term if data.Term else None,
            academic_session=data.AcademicSession.session if data.AcademicSession else None
        ) for data in result_data
    ]


@student_result_data_router.get("/{result_data_id}", response=StudentResultDataResponseSchema)
def get_student_result_data(request, result_data_id: int):
    """Get specific student result data by ID"""
    data = get_object_or_404(
        Student_Result_Data.objects.select_related('Student_name', 'Term', 'AcademicSession'),
        id=result_data_id
    )
    return StudentResultDataResponseSchema(
        id=data.pk,
        total_score=data.TotalScore if data.TotalScore is not None else "-",
        total_number=data.Totalnumber if data.Totalnumber is not None else "-",
        average=data.Average if data.Average is not None else "-",
        position=data.Position if data.Position is not None else "-",
        remark=data.Remark if data.Remark is not None else "-",
        published=data.published,
        student_name=data.Student_name.student_name if data.Student_name else None,
        term=data.Term.term if data.Term else None,
        academic_session=data.AcademicSession.session if data.AcademicSession else None
    )


@student_result_data_router.post("/", response=StudentResultDataResponseSchema)
def create_student_result_data(request, payload: StudentResultDataCreateSchema):
    """Create new student result data"""
    student = get_object_or_404(Students_Pin_and_ID, id=payload.student_name_id)
    term = get_object_or_404(Term, id=payload.term_id) if payload.term_id else None
    academic_session = get_object_or_404(AcademicSession, id=payload.academic_session_id) if payload.academic_session_id else None
    
    data = Student_Result_Data.objects.create(
        Student_name=student,
        TotalScore=payload.total_score,
        Totalnumber=payload.total_number,
        Average=payload.average,
        Position=payload.position,
        Remark=payload.remark,
        Term=term,
        AcademicSession=academic_session,
        published=payload.published
    )
    
    return StudentResultDataResponseSchema(
        id=data.pk,
        total_score=data.TotalScore if data.TotalScore is not None else "-",
        total_number=data.Totalnumber if data.Totalnumber is not None else "-",
        average=data.Average if data.Average is not None else "-",
        position=data.Position if data.Position is not None else "-",
        remark=data.Remark if data.Remark is not None else "-",
        published=data.published,
        student_name=data.Student_name.student_name if data.Student_name else None,
        term=data.Term.term if data.Term else None,
        academic_session=data.AcademicSession.session if data.AcademicSession else None
    )


@student_result_data_router.put("/{result_data_id}", response=StudentResultDataResponseSchema)
def update_student_result_data(request, result_data_id: int, payload: StudentResultDataUpdateSchema):
    """Update existing student result data"""
    data = get_object_or_404(Student_Result_Data, id=result_data_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    if 'student_name_id' in update_data:
        student = get_object_or_404(Students_Pin_and_ID, id=update_data['student_name_id'])
        data.Student_name = student
    
    if 'term_id' in update_data:
        term = get_object_or_404(Term, id=update_data['term_id']) if update_data['term_id'] else None
        data.Term = term
    
    if 'academic_session_id' in update_data:
        academic_session = get_object_or_404(AcademicSession, id=update_data['academic_session_id']) if update_data['academic_session_id'] else None
        data.AcademicSession = academic_session
    
    # Update other fields
    field_mapping = {
        'total_score': 'TotalScore',
        'total_number': 'Totalnumber',
        'average': 'Average',
        'position': 'Position',
        'remark': 'Remark',
        'published': 'published'
    }
    
    for key, value in update_data.items():
        if key in field_mapping:
            setattr(data, field_mapping[key], value)
    
    data.save()
    
    return StudentResultDataResponseSchema(
        id=data.pk,
        total_score=data.TotalScore if data.TotalScore is not None else "-",
        total_number=data.Totalnumber if data.Totalnumber is not None else "-",
        average=data.Average if data.Average is not None else "-",
        position=data.Position if data.Position is not None else "-",
        remark=data.Remark if data.Remark is not None else "-",
        published=data.published,
        student_name=data.Student_name.student_name if data.Student_name else None,
        term=data.Term.term if data.Term else None,
        academic_session=data.AcademicSession.session if data.AcademicSession else None
    )


@student_result_data_router.delete("/{result_data_id}", response=StudentResultDataDeleteSchema)
def delete_student_result_data(request, result_data_id: int):
    """Delete student result data"""
    data = get_object_or_404(Student_Result_Data, id=result_data_id)
    data.delete()
    return StudentResultDataDeleteSchema(deleted_id=result_data_id)


# Result routes
@result_router.get("/", response=List[ResultResponseSchema])
def list_results(request):
    """Get all results"""
    results = Result.objects.select_related('student', 'student_class', 'Subject').all()
    return [
        ResultResponseSchema(
            id=result.pk,
            first_test=result.FirstTest if result.FirstTest is not None else "-",
            first_ass=result.FirstAss if result.FirstAss is not None else "-",
            mid_term_test=result.MidTermTest if result.MidTermTest is not None else "-",
            second_ass=result.SecondAss if result.SecondAss is not None else "-",
            second_test=result.SecondTest if result.SecondTest is not None else "-",
            ca=result.CA if result.CA is not None else "-",
            exam=result.Exam if result.Exam is not None else "-",
            total=result.Total if result.Total is not None else "-",
            grade=result.Grade if result.Grade is not None else "-",
            subject_position=result.SubjectPosition if result.SubjectPosition is not None else "-",
            remark=result.Remark if result.Remark is not None else "-",
            published=result.published,
            student_name=result.student.student_name if result.student else None,
            student_class_name=result.student_class.Class if result.student_class else None,
            subject_name=result.Subject.subject_name if result.Subject else None
        ) for result in results
    ]


@result_router.get("/{result_id}", response=ResultResponseSchema)
def get_result(request, result_id: int):
    """Get specific result by ID"""
    result = get_object_or_404(
        Result.objects.select_related('student', 'student_class', 'Subject'),
        id=result_id
    )
    return ResultResponseSchema(
        id=result.pk,
        first_test=result.FirstTest if result.FirstTest is not None else "-",
        first_ass=result.FirstAss if result.FirstAss is not None else "-",
        mid_term_test=result.MidTermTest if result.MidTermTest is not None else "-",
        second_ass=result.SecondAss if result.SecondAss is not None else "-",
        second_test=result.SecondTest if result.SecondTest is not None else "-",
        ca=result.CA if result.CA is not None else "-",
        exam=result.Exam if result.Exam is not None else "-",
        total=result.Total if result.Total is not None else "-",
        grade=result.Grade if result.Grade is not None else "-",
        subject_position=result.SubjectPosition if result.SubjectPosition is not None else "-",
        remark=result.Remark if result.Remark is not None else "-",
        published=result.published, 
        student_name=result.student.student_name if result.student else None,
        student_class_name=result.student_class.Class if result.student_class else None,
        subject_name=result.Subject.subject_name if result.Subject else None
    )


@result_router.post("/", response=ResultResponseSchema)
def create_result(request, payload: ResultCreateSchema):
    """Create new result"""
    student = get_object_or_404(Students_Pin_and_ID, id=payload.student_id)
    student_class = get_object_or_404(Class, id=payload.student_class_id) if payload.student_class_id else None
    subject = get_object_or_404(Subject, id=payload.subject_id)
    result_summary = get_object_or_404(Student_Result_Data, id=payload.students_result_summary_id) if payload.students_result_summary_id else None
    
    result = Result.objects.create(
        student=student,
        student_class=student_class,
        students_result_summary=result_summary,
        Subject=subject,
        FirstTest=payload.first_test,
        FirstAss=payload.first_ass,
        MidTermTest=payload.mid_term_test,
        SecondAss=payload.second_ass,
        SecondTest=payload.second_test,
        CA=payload.ca,
        Exam=payload.exam,
        Total=payload.total,
        Grade=payload.grade,
        SubjectPosition=payload.subject_position,
        Remark=payload.remark,
        published=payload.published
    )
    
    return ResultResponseSchema(
        id=result.pk,
        first_test=result.FirstTest if result.FirstTest is not None else "-",
        first_ass=result.FirstAss if result.FirstAss is not None else "-",
        mid_term_test=result.MidTermTest if result.MidTermTest is not None else "-",
        second_ass=result.SecondAss if result.SecondAss is not None else "-",
        second_test=result.SecondTest if result.SecondTest is not None else "-",
        ca=result.CA if result.CA is not None else "-",
        exam=result.Exam if result.Exam is not None else "-",
        total=result.Total if result.Total is not None else "-",
        grade=result.Grade if result.Grade is not None else "-",
        subject_position=result.SubjectPosition if result.SubjectPosition is not None else "-",
        remark=result.Remark if result.Remark is not None else "-",
        published=result.published,
        student_name=result.student.student_name,
        student_class_name=result.student_class.Class if result.student_class else None,
        subject_name=result.Subject.subject_name
    )


@result_router.put("/{result_id}", response=ResultResponseSchema)
def update_result(request, result_id: int, payload: ResultUpdateSchema):
    """Update existing result"""
    result = get_object_or_404(Result, id=result_id)
    
    update_data = payload.dict(exclude_unset=True)
    
    # Update foreign keys
    if 'student_id' in update_data:
        student = get_object_or_404(Students_Pin_and_ID, id=update_data['student_id'])
        result.student = student
    
    if 'student_class_id' in update_data:
        student_class = get_object_or_404(Class, id=update_data['student_class_id']) if update_data['student_class_id'] else None
        result.student_class = student_class
    
    if 'subject_id' in update_data:
        subject = get_object_or_404(Subject, id=update_data['subject_id'])
        result.Subject = subject
    
    if 'students_result_summary_id' in update_data:
        result_summary = get_object_or_404(Student_Result_Data, id=update_data['students_result_summary_id']) if update_data['students_result_summary_id'] else None
        result.students_result_summary = result_summary
    
    # Update other fields
    field_mapping = {
        'first_test': 'FirstTest',
        'first_ass': 'FirstAss',
        'mid_term_test': 'MidTermTest',
        'second_ass': 'SecondAss',
        'second_test': 'SecondTest',
        'ca': 'CA',
        'exam': 'Exam',
        'total': 'Total',
        'grade': 'Grade',
        'subject_position': 'SubjectPosition',
        'remark': 'Remark',
        'published': 'published'
    }
    
    for key, value in update_data.items():
        if key in field_mapping:
            setattr(result, field_mapping[key], value)
    
    result.save()
    
    return ResultResponseSchema(
        id=result.pk,
        first_test=result.FirstTest if result.FirstTest is not None else "-",
        first_ass=result.FirstAss if result.FirstAss is not None else "-",
        mid_term_test=result.MidTermTest if result.MidTermTest is not None else "-",
        second_ass=result.SecondAss if result.SecondAss is not None else "-",
        second_test=result.SecondTest if result.SecondTest is not None else "-",
        ca=result.CA if result.CA is not None else "-",
        exam=result.Exam if result.Exam is not None else "-",
        total=result.Total if result.Total is not None else "-",
        grade=result.Grade if result.Grade is not None else "-",
        subject_position=result.SubjectPosition if result.SubjectPosition is not None else "-",
        remark=result.Remark if result.Remark is not None else "-",
        published=result.published,
        student_name=result.student.student_name if result.student else None,
        student_class_name=result.student_class.Class if result.student_class else None,
        subject_name=result.Subject.subject_name if result.Subject else None
    )


@result_router.delete("/{result_id}", response=ResultDeleteSchema)
def delete_result(request, result_id: int):
    """Delete result"""
    result = get_object_or_404(Result, id=result_id)
    result.delete()
    return ResultDeleteSchema(deleted_id=result_id)
