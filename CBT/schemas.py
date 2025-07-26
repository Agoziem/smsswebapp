from typing import Optional, List
from ninja import ModelSchema, Schema, Field

from .models import Test, Answer, Question, QuestionSet, QuestionSetGroup, TestSetGroup, TestQuestionSet


# Test Schemas
class TestResponseSchema(ModelSchema):
    class Meta:
        model = Test
        fields = '__all__'


class TestCreateSchema(Schema):
    """Schema for creating a new test"""
    name: str = Field(..., max_length=255, description="Test name")


class TestUpdateSchema(Schema):
    """Schema for updating a test"""
    name: Optional[str] = Field(None, max_length=255, description="Test name")


# Answer Schemas
class AnswerResponseSchema(ModelSchema):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerCreateSchema(Schema):
    """Schema for creating a new answer"""
    answerId: str = Field(..., max_length=100, description="Answer ID")
    answertext: str = Field(..., max_length=255, description="Answer text")
    isCorrect: bool = Field(default=False, description="Is this the correct answer")


class AnswerUpdateSchema(Schema):
    """Schema for updating an answer"""
    answerId: Optional[str] = Field(None, max_length=100, description="Answer ID")
    answertext: Optional[str] = Field(None, max_length=255, description="Answer text")
    isCorrect: Optional[bool] = Field(None, description="Is this the correct answer")


# Question Schemas
class QuestionResponseSchema(ModelSchema):
    answers: List[AnswerResponseSchema] = Field(default_factory=list, description="List of answers")
    
    class Meta:
        model = Question
        fields = '__all__'


class QuestionCreateSchema(Schema):
    """Schema for creating a new question"""
    questionId: str = Field(..., max_length=100, description="Question ID")
    questiontext: str = Field(..., description="Question text content")
    questionMark: int = Field(default=0, description="Question marks")
    required: bool = Field(default=True, description="Is this question required")
    answer_ids: List[int] = Field(default_factory=list, description="List of answer IDs")


class QuestionUpdateSchema(Schema):
    """Schema for updating a question"""
    questionId: Optional[str] = Field(None, max_length=100, description="Question ID")
    questiontext: Optional[str] = Field(None, description="Question text content")
    questionMark: Optional[int] = Field(None, description="Question marks")
    required: Optional[bool] = Field(None, description="Is this question required")
    answer_ids: Optional[List[int]] = Field(None, description="List of answer IDs")


# QuestionSet Schemas
class QuestionSetResponseSchema(ModelSchema):
    exam_classes: List[str] = Field(default_factory=list, description="List of class names")
    questions: List[QuestionResponseSchema] = Field(default_factory=list, description="List of questions")
    
    class Meta:
        model = QuestionSet
        fields = '__all__'


class QuestionSetCreateSchema(Schema):
    """Schema for creating a new question set"""
    examTime: int = Field(default=0, description="Exam time in minutes")
    exam_class_ids: List[int] = Field(default_factory=list, description="List of class IDs")
    subject_id: int = Field(..., description="Subject ID")
    teacher_id: int = Field(..., description="Teacher ID")
    question_ids: List[int] = Field(default_factory=list, description="List of question IDs")


class QuestionSetUpdateSchema(Schema):
    """Schema for updating a question set"""
    examTime: Optional[int] = Field(None, description="Exam time in minutes")
    exam_class_ids: Optional[List[int]] = Field(None, description="List of class IDs")
    subject_id: Optional[int] = Field(None, description="Subject ID")
    teacher_id: Optional[int] = Field(None, description="Teacher ID")
    question_ids: Optional[List[int]] = Field(None, description="List of question IDs")


# QuestionSetGroup Schemas  
class QuestionSetGroupResponseSchema(ModelSchema):
    question_sets: List[QuestionSetResponseSchema] = Field(default_factory=list, description="List of question sets")
    
    class Meta:
        model = QuestionSetGroup
        fields = '__all__'


class QuestionSetGroupCreateSchema(Schema):
    """Schema for creating a new question set group"""
    name: str = Field(..., max_length=255, description="Question set group name")
    date: str = Field(..., description="Date of the test")
    question_set_ids: List[int] = Field(default_factory=list, description="List of question set IDs")
    test_id: int = Field(..., description="Test ID")


class QuestionSetGroupUpdateSchema(Schema):
    """Schema for updating a question set group"""
    name: Optional[str] = Field(None, max_length=255, description="Question set group name")
    date: Optional[str] = Field(None, description="Date of the test")
    question_set_ids: Optional[List[int]] = Field(None, description="List of question set IDs")
    test_id: Optional[int] = Field(None, description="Test ID")


# TestSetGroup Schemas (Students CBT Models)
class TestSetGroupResponseSchema(ModelSchema):
    class Meta:
        model = TestSetGroup
        fields = '__all__'


class TestSetGroupCreateSchema(Schema):
    """Schema for creating a new test set group"""
    name: str = Field(..., max_length=255, description="Test set group name")
    timeUsedForTest: int = Field(default=0, description="Time used for test in minutes")
    student_id: int = Field(..., description="Student ID")
    testClass_id: int = Field(..., description="Test class ID")
    test_id: int = Field(..., description="Test ID")


class TestSetGroupUpdateSchema(Schema):
    """Schema for updating a test set group"""
    name: Optional[str] = Field(None, max_length=255, description="Test set group name")
    timeUsedForTest: Optional[int] = Field(None, description="Time used for test in minutes")
    student_id: Optional[int] = Field(None, description="Student ID")
    testClass_id: Optional[int] = Field(None, description="Test class ID")
    test_id: Optional[int] = Field(None, description="Test ID")


# TestQuestionSet Schemas
class TestQuestionSetResponseSchema(ModelSchema):
    class Meta:
        model = TestQuestionSet
        fields = '__all__'


class TestQuestionSetCreateSchema(Schema):
    """Schema for creating a new test question set"""
    testTotalScore: int = Field(default=0, description="Total score for test")
    testSubject_id: int = Field(..., description="Test subject ID")
    testSetGroup_id: int = Field(..., description="Test set group ID")


class TestQuestionSetUpdateSchema(Schema):
    """Schema for updating a test question set"""
    testTotalScore: Optional[int] = Field(None, description="Total score for test")
    testSubject_id: Optional[int] = Field(None, description="Test subject ID")
    testSetGroup_id: Optional[int] = Field(None, description="Test set group ID")


# Common response schemas
class ErrorResponseSchema(Schema):
    error: str


class SuccessResponseSchema(Schema):
    message: str