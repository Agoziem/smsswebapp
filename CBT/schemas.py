from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from datetime import date as date_type


# Test Schemas
class TestBase(BaseModel):
    name: str = Field(..., max_length=255, description="Test name")


class TestCreateSchema(TestBase):
    """Schema for creating a new test"""
    pass


class TestUpdateSchema(BaseModel):
    """Schema for updating a test"""
    name: Optional[str] = Field(None, max_length=255, description="Test name")


class TestResponseSchema(TestBase):
    """Schema for test response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class TestDeleteSchema(BaseModel):
    """Schema for test deletion confirmation"""
    message: str = Field(default="Test deleted successfully")
    deleted_id: int


# Answer Schemas
class AnswerBase(BaseModel):
    answer_id: str = Field(..., max_length=100, description="Answer ID")
    answer_text: str = Field(..., max_length=255, description="Answer text")
    is_correct: bool = Field(default=False, description="Is this the correct answer")


class AnswerCreateSchema(AnswerBase):
    """Schema for creating a new answer"""
    pass


class AnswerUpdateSchema(BaseModel):
    """Schema for updating an answer"""
    answer_id: Optional[str] = Field(None, max_length=100, description="Answer ID")
    answer_text: Optional[str] = Field(None, max_length=255, description="Answer text")
    is_correct: Optional[bool] = Field(None, description="Is this the correct answer")


class AnswerResponseSchema(AnswerBase):
    """Schema for answer response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class AnswerDeleteSchema(BaseModel):
    """Schema for answer deletion confirmation"""
    message: str = Field(default="Answer deleted successfully")
    deleted_id: int


# Question Schemas
class QuestionBase(BaseModel):
    question_id: str = Field(..., max_length=100, description="Question ID")
    question_text: str = Field(..., description="Question text content")
    question_mark: int = Field(default=0, description="Question marks")
    required: bool = Field(default=True, description="Is this question required")


class QuestionCreateSchema(QuestionBase):
    """Schema for creating a new question"""
    answer_ids: List[int] = Field(default_factory=list, description="List of answer IDs")


class QuestionUpdateSchema(BaseModel):
    """Schema for updating a question"""
    question_id: Optional[str] = Field(None, max_length=100, description="Question ID")
    question_text: Optional[str] = Field(None, description="Question text content")
    question_mark: Optional[int] = Field(None, description="Question marks")
    required: Optional[bool] = Field(None, description="Is this question required")
    answer_ids: Optional[List[int]] = Field(None, description="List of answer IDs")


class QuestionResponseSchema(QuestionBase):
    """Schema for question response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    answers: List[AnswerResponseSchema] = Field(default_factory=list, description="List of answers")


class QuestionDeleteSchema(BaseModel):
    """Schema for question deletion confirmation"""
    message: str = Field(default="Question deleted successfully")
    deleted_id: int


# QuestionSet Schemas
class QuestionSetBase(BaseModel):
    exam_time: int = Field(default=0, description="Exam time in minutes")


class QuestionSetCreateSchema(QuestionSetBase):
    """Schema for creating a new question set"""
    exam_class_ids: List[int] = Field(default_factory=list, description="List of class IDs")
    subject_id: int = Field(..., description="Subject ID")
    teacher_id: int = Field(..., description="Teacher ID")
    question_ids: List[int] = Field(default_factory=list, description="List of question IDs")


class QuestionSetUpdateSchema(BaseModel):
    """Schema for updating a question set"""
    exam_time: Optional[int] = Field(None, description="Exam time in minutes")
    exam_class_ids: Optional[List[int]] = Field(None, description="List of class IDs")
    subject_id: Optional[int] = Field(None, description="Subject ID")
    teacher_id: Optional[int] = Field(None, description="Teacher ID")
    question_ids: Optional[List[int]] = Field(None, description="List of question IDs")


class QuestionSetResponseSchema(QuestionSetBase):
    """Schema for question set response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    subject_name: Optional[str] = Field(None, description="Subject name")
    teacher_name: Optional[str] = Field(None, description="Teacher name")
    exam_classes: List[str] = Field(default_factory=list, description="List of class names")
    questions: List[QuestionResponseSchema] = Field(default_factory=list, description="List of questions")


class QuestionSetDeleteSchema(BaseModel):
    """Schema for question set deletion confirmation"""
    message: str = Field(default="Question set deleted successfully")
    deleted_id: int


# QuestionSetGroup Schemas
class QuestionSetGroupBase(BaseModel):
    name: str = Field(..., max_length=255, description="Question set group name")
    date: date_type = Field(..., description="Date of the test")


class QuestionSetGroupCreateSchema(QuestionSetGroupBase):
    """Schema for creating a new question set group"""
    question_set_ids: List[int] = Field(default_factory=list, description="List of question set IDs")
    test_id: int = Field(..., description="Test ID")


class QuestionSetGroupUpdateSchema(BaseModel):
    """Schema for updating a question set group"""
    name: Optional[str] = Field(None, max_length=255, description="Question set group name")
    date: Optional[date_type] = Field(None, description="Date of the test")
    question_set_ids: Optional[List[int]] = Field(None, description="List of question set IDs")
    test_id: Optional[int] = Field(None, description="Test ID")


class QuestionSetGroupResponseSchema(QuestionSetGroupBase):
    """Schema for question set group response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    test_name: Optional[str] = Field(None, description="Test name")
    question_sets: List[QuestionSetResponseSchema] = Field(default_factory=list, description="List of question sets")


class QuestionSetGroupDeleteSchema(BaseModel):
    """Schema for question set group deletion confirmation"""
    message: str = Field(default="Question set group deleted successfully")
    deleted_id: int


# TestSetGroup Schemas (Students CBT Models)
class TestSetGroupBase(BaseModel):
    name: str = Field(..., max_length=255, description="Test set group name")
    time_used_for_test: int = Field(default=0, description="Time used for test in minutes")


class TestSetGroupCreateSchema(TestSetGroupBase):
    """Schema for creating a new test set group"""
    student_id: int = Field(..., description="Student ID")
    test_class_id: int = Field(..., description="Test class ID")
    test_id: int = Field(..., description="Test ID")


class TestSetGroupUpdateSchema(BaseModel):
    """Schema for updating a test set group"""
    name: Optional[str] = Field(None, max_length=255, description="Test set group name")
    time_used_for_test: Optional[int] = Field(None, description="Time used for test in minutes")
    student_id: Optional[int] = Field(None, description="Student ID")
    test_class_id: Optional[int] = Field(None, description="Test class ID")
    test_id: Optional[int] = Field(None, description="Test ID")


class TestSetGroupResponseSchema(TestSetGroupBase):
    """Schema for test set group response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    student_name: Optional[str] = Field(None, description="Student name")
    test_class_name: Optional[str] = Field(None, description="Test class name")
    test_name: Optional[str] = Field(None, description="Test name")


class TestSetGroupDeleteSchema(BaseModel):
    """Schema for test set group deletion confirmation"""
    message: str = Field(default="Test set group deleted successfully")
    deleted_id: int


# TestQuestionSet Schemas
class TestQuestionSetBase(BaseModel):
    test_total_score: int = Field(default=0, description="Total score for test")


class TestQuestionSetCreateSchema(TestQuestionSetBase):
    """Schema for creating a new test question set"""
    test_subject_id: int = Field(..., description="Test subject ID")
    test_set_group_id: int = Field(..., description="Test set group ID")


class TestQuestionSetUpdateSchema(BaseModel):
    """Schema for updating a test question set"""
    test_total_score: Optional[int] = Field(None, description="Total score for test")
    test_subject_id: Optional[int] = Field(None, description="Test subject ID")
    test_set_group_id: Optional[int] = Field(None, description="Test set group ID")


class TestQuestionSetResponseSchema(TestQuestionSetBase):
    """Schema for test question set response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    test_subject_name: Optional[str] = Field(None, description="Test subject name")
    test_set_group_name: Optional[str] = Field(None, description="Test set group name")


class TestQuestionSetDeleteSchema(BaseModel):
    """Schema for test question set deletion confirmation"""
    message: str = Field(default="Test question set deleted successfully")
    deleted_id: int