from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from typing import List

from ..models import AcademicSession, Term, Class, Subject
from ..schemas import (
    AcademicSessionCreateSchema,
    AcademicSessionUpdateSchema,
    AcademicSessionResponseSchema,
    AcademicSessionDeleteSchema,
    TermCreateSchema,
    TermUpdateSchema,
    TermResponseSchema,
    TermDeleteSchema,
    ClassCreateSchema,
    ClassUpdateSchema,
    ClassResponseSchema,
    ClassDeleteSchema,
    SubjectCreateSchema,
    SubjectUpdateSchema,
    SubjectResponseSchema,
    SubjectDeleteSchema
)

academic_session_router = Router(tags=["Academic Sessions"])
term_router = Router(tags=["Terms"])
class_router = Router(tags=["Classes"])
subject_router = Router(tags=["Subjects"])


# Academic Session routes
@academic_session_router.get("/", response=List[AcademicSessionResponseSchema])
def list_academic_sessions(request):
    """Get all academic sessions"""
    sessions = AcademicSession.objects.all()
    return [AcademicSessionResponseSchema.model_validate(session) for session in sessions]


@academic_session_router.get("/{session_id}", response=AcademicSessionResponseSchema)
def get_academic_session(request, session_id: int):
    """Get a specific academic session by ID"""
    session = get_object_or_404(AcademicSession, id=session_id)
    return AcademicSessionResponseSchema.model_validate(session)


@academic_session_router.post("/", response=AcademicSessionResponseSchema)
def create_academic_session(request, payload: AcademicSessionCreateSchema):
    """Create a new academic session"""
    session = AcademicSession.objects.create(**payload.dict())
    return AcademicSessionResponseSchema.model_validate(session)


@academic_session_router.put("/{session_id}", response=AcademicSessionResponseSchema)
def update_academic_session(request, session_id: int, payload: AcademicSessionUpdateSchema):
    """Update an existing academic session"""
    session = get_object_or_404(AcademicSession, id=session_id)
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(session, key, value)
    
    session.save()
    return AcademicSessionResponseSchema.model_validate(session)


@academic_session_router.delete("/{session_id}", response=AcademicSessionDeleteSchema)
def delete_academic_session(request, session_id: int):
    """Delete an academic session"""
    session = get_object_or_404(AcademicSession, id=session_id)
    session.delete()
    return AcademicSessionDeleteSchema(deleted_id=session_id)


# Term routes
@term_router.get("/", response=List[TermResponseSchema])
def list_terms(request):
    """Get all terms"""
    terms = Term.objects.all()
    return [TermResponseSchema.model_validate(term) for term in terms]


@term_router.get("/{term_id}", response=TermResponseSchema)
def get_term(request, term_id: int):
    """Get a specific term by ID"""
    term = get_object_or_404(Term, id=term_id)
    return TermResponseSchema.model_validate(term)


@term_router.post("/", response=TermResponseSchema)
def create_term(request, payload: TermCreateSchema):
    """Create a new term"""
    term = Term.objects.create(**payload.dict())
    return TermResponseSchema.model_validate(term)


@term_router.put("/{term_id}", response=TermResponseSchema)
def update_term(request, term_id: int, payload: TermUpdateSchema):
    """Update an existing term"""
    term = get_object_or_404(Term, id=term_id)
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(term, key, value)
    
    term.save()
    return TermResponseSchema.model_validate(term)


@term_router.delete("/{term_id}", response=TermDeleteSchema)
def delete_term(request, term_id: int):
    """Delete a term"""
    term = get_object_or_404(Term, id=term_id)
    term.delete()
    return TermDeleteSchema(deleted_id=term_id)


# Class routes
@class_router.get("/", response=List[ClassResponseSchema])
def list_classes(request):
    """Get all classes"""
    classes = Class.objects.all()
    return [
        ClassResponseSchema(
            id=cls.pk,
            class_name=cls.Class
        ) for cls in classes
    ]


@class_router.get("/{class_id}", response=ClassResponseSchema)
def get_class(request, class_id: int):
    """Get a specific class by ID"""
    cls = get_object_or_404(Class, id=class_id)
    return ClassResponseSchema(
        id=cls.pk,
        class_name=cls.Class
    )


@class_router.post("/", response=ClassResponseSchema)
def create_class(request, payload: ClassCreateSchema):
    """Create a new class"""
    cls = Class.objects.create(Class=payload.class_name)
    return ClassResponseSchema(
        id=cls.pk,
        class_name=cls.Class
    )


@class_router.put("/{class_id}", response=ClassResponseSchema)
def update_class(request, class_id: int, payload: ClassUpdateSchema):
    """Update an existing class"""
    cls = get_object_or_404(Class, id=class_id)
    
    update_data = payload.dict(exclude_unset=True)
    if 'class_name' in update_data:
        cls.Class = update_data['class_name']
    
    cls.save()
    return ClassResponseSchema(
        id=cls.pk,
        class_name=cls.Class
    )


@class_router.delete("/{class_id}", response=ClassDeleteSchema)
def delete_class(request, class_id: int):
    """Delete a class"""
    cls = get_object_or_404(Class, id=class_id)
    cls.delete()
    return ClassDeleteSchema(deleted_id=class_id)


# Subject routes
@subject_router.get("/", response=List[SubjectResponseSchema])
def list_subjects(request):
    """Get all subjects"""
    subjects = Subject.objects.all()
    return [SubjectResponseSchema.model_validate(subject) for subject in subjects]


@subject_router.get("/{subject_id}", response=SubjectResponseSchema)
def get_subject(request, subject_id: int):
    """Get a specific subject by ID"""
    subject = get_object_or_404(Subject, id=subject_id)
    return SubjectResponseSchema.model_validate(subject)


@subject_router.post("/", response=SubjectResponseSchema)
def create_subject(request, payload: SubjectCreateSchema):
    """Create a new subject"""
    subject = Subject.objects.create(**payload.dict())
    return SubjectResponseSchema.model_validate(subject)


@subject_router.put("/{subject_id}", response=SubjectResponseSchema)
def update_subject(request, subject_id: int, payload: SubjectUpdateSchema):
    """Update an existing subject"""
    subject = get_object_or_404(Subject, id=subject_id)
    
    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(subject, key, value)
    
    subject.save()
    return SubjectResponseSchema.model_validate(subject)


@subject_router.delete("/{subject_id}", response=SubjectDeleteSchema)
def delete_subject(request, subject_id: int):
    """Delete a subject"""
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    return SubjectDeleteSchema(deleted_id=subject_id)
