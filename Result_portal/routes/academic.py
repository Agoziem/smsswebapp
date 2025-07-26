from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from ninja_extra import api_controller, route

from ..models import AcademicSession, Term, Class, Subject
from ..schemas import (
    AcademicSessionCreateSchema,
    AcademicSessionUpdateSchema,
    AcademicSessionResponseSchema,
    TermCreateSchema,
    TermUpdateSchema,
    TermResponseSchema,
    ClassCreateSchema,
    ClassUpdateSchema,
    ClassResponseSchema,
    SubjectCreateSchema,
    SubjectUpdateSchema,
    SubjectResponseSchema,
    SuccessResponseSchema
)

@api_controller("/academic-sessions", tags=["Academic Sessions"])
class AcademicSessionController:

    @route.get("/", response=List[AcademicSessionResponseSchema])
    def list_academic_sessions(self):
        """Get all academic sessions"""
        return AcademicSession.objects.all()

    @route.get("/{session_id}", response=AcademicSessionResponseSchema)
    def get_academic_session(self, session_id: int):
        """Get a specific academic session by ID"""
        return get_object_or_404(AcademicSession, id=session_id)

    @route.post("/", response=AcademicSessionResponseSchema)
    def create_academic_session(self, payload: AcademicSessionCreateSchema):
        """Create a new academic session"""
        return AcademicSession.objects.create(**payload.model_dump())

    @route.put("/{session_id}", response=AcademicSessionResponseSchema)
    def update_academic_session(self, session_id: int, payload: AcademicSessionUpdateSchema):
        """Update an existing academic session"""
        session = get_object_or_404(AcademicSession, id=session_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(session, key, value)
        
        session.save()
        return session

    @route.delete("/{session_id}", response={200: SuccessResponseSchema, 404: "Academic Session not found"})
    def delete_academic_session(self, session_id: int):
        """Delete an academic session"""
        session = get_object_or_404(AcademicSession, id=session_id)
        session.delete()
        return {"message": "Academic session deleted successfully"}


@api_controller("/terms", tags=["Terms"])
class TermController:

    @route.get("/", response=List[TermResponseSchema])
    def list_terms(self):
        """Get all terms"""
        return Term.objects.all()

    @route.get("/{term_id}", response=TermResponseSchema)
    def get_term(self, term_id: int):
        """Get a specific term by ID"""
        return get_object_or_404(Term, id=term_id)

    @route.post("/", response=TermResponseSchema)
    def create_term(self, payload: TermCreateSchema):
        """Create a new term"""
        return Term.objects.create(**payload.model_dump())

    @route.put("/{term_id}", response=TermResponseSchema)
    def update_term(self, term_id: int, payload: TermUpdateSchema):
        """Update an existing term"""
        term = get_object_or_404(Term, id=term_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(term, key, value)
        
        term.save()
        return term

    @route.delete("/{term_id}", response={200: SuccessResponseSchema, 404: "Term not found"})
    def delete_term(self, term_id: int):
        """Delete a term"""
        term = get_object_or_404(Term, id=term_id)
        term.delete()
        return {"message": "Term deleted successfully"}


@api_controller("/classes", tags=["Classes"])
class ClassController:

    @route.get("/", response=List[ClassResponseSchema])
    def list_classes(self):
        """Get all classes"""
        return Class.objects.all()

    @route.get("/{class_id}", response=ClassResponseSchema)
    def get_class(self, class_id: int):
        """Get a specific class by ID"""
        return get_object_or_404(Class, id=class_id)

    @route.post("/", response=ClassResponseSchema)
    def create_class(self, payload: ClassCreateSchema):
        """Create a new class"""
        return Class.objects.create(**payload.model_dump())

    @route.put("/{class_id}", response=ClassResponseSchema)
    def update_class(self, class_id: int, payload: ClassUpdateSchema):
        """Update an existing class"""
        class_obj = get_object_or_404(Class, id=class_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(class_obj, key, value)
        
        class_obj.save()
        return class_obj

    @route.delete("/{class_id}", response={200: SuccessResponseSchema, 404: "Class not found"})
    def delete_class(self, class_id: int):
        """Delete a class"""
        class_obj = get_object_or_404(Class, id=class_id)
        class_obj.delete()
        return {"message": "Class deleted successfully"}


@api_controller("/subjects", tags=["Subjects"])
class SubjectController:

    @route.get("/", response=List[SubjectResponseSchema])
    def list_subjects(self):
        """Get all subjects"""
        return Subject.objects.all()

    @route.get("/{subject_id}", response=SubjectResponseSchema)
    def get_subject(self, subject_id: int):
        """Get a specific subject by ID"""
        return get_object_or_404(Subject, id=subject_id)

    @route.post("/", response=SubjectResponseSchema)
    def create_subject(self, payload: SubjectCreateSchema):
        """Create a new subject"""
        return Subject.objects.create(**payload.model_dump())

    @route.put("/{subject_id}", response=SubjectResponseSchema)
    def update_subject(self, subject_id: int, payload: SubjectUpdateSchema):
        """Update an existing subject"""
        subject = get_object_or_404(Subject, id=subject_id)
        
        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(subject, key, value)
        
        subject.save()
        return subject

    @route.delete("/{subject_id}", response={200: SuccessResponseSchema, 404: "Subject not found"})
    def delete_subject(self, subject_id: int):
        """Delete a subject"""
        subject = get_object_or_404(Subject, id=subject_id)
        subject.delete()
        return {"message": "Subject deleted successfully"}
