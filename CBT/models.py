from django.db import models
from Result_portal.models import Students_Pin_and_ID,Class
from Home.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=255,default="",blank=False)
    code = models.CharField(max_length=10,default="",blank=False)

    def __str__(self):
        return str(self.name)

class Exam(models.Model):
    name = models.CharField(max_length=255,default="",blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.name)

class ExamClass(models.Model):
    name = models.OneToOneField(Class,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    # Add other fields as needed

# Question Set can be only one Class and Subject
class QuestionSet(models.Model):
    name = models.CharField(max_length=255,default="No Subject",blank=False)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    exam_class = models.ForeignKey(ExamClass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


# A Question Section Set can have different Questions
class Question(models.Model):
    text = models.CharField(max_length=1000,default="",blank=False)
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.question_set)

class Answer(models.Model):
    text = models.CharField(max_length=255,default="",blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} Answer: {self.text}"
    # Add other fields as needed





# The Particular Exam in Question
class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exam)
    # Add other fields as needed


class ExamAnswer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exam)
    # Add other fields as needed


class StudentExam(models.Model):
    student = models.ForeignKey(Students_Pin_and_ID, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.exam)
    # Add other fields as needed