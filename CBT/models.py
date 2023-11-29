from django.db import models
from Result_portal.models import Students_Pin_and_ID,Class,Subject
from Teachers_Portal.models import Teacher
from ckeditor.fields import RichTextField
from django.utils import timezone
# Teachers CBT Models (Models for Setting)

class Test(models.Model):
    name = models.CharField(max_length=255, default="None",blank=False)

    def __str__(self):
        return str(self.name)


class Answer(models.Model):
    answerId=models.CharField(max_length=100,default="None",blank=False)
    answertext = models.CharField(max_length=255,default="None",blank=False)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answertext}"
    
class Question(models.Model):
    questionId=models.CharField(max_length=100,default="None",blank=False)
    questiontext = RichTextField(default="None",blank=False,null=True)
    questionMark = models.IntegerField(default=0,blank=True)
    required=models.BooleanField(default=True)
    answers = models.ManyToManyField(Answer)

    
    def __str__(self):
        return str(self.questiontext)
    
    class Meta:
        ordering = ['id']

class QuestionSet(models.Model):
    ExamClass = models.ManyToManyField(Class,blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    examTime = models.IntegerField(default=0,blank=True)
    questions= models.ManyToManyField(Question,blank=True)

    def __str__(self):
        return  f'{self.subject.subject_name}'
      
class QuestionSetGroup(models.Model):
    questionsets=models.ManyToManyField(QuestionSet, related_name='questionsets',blank=True)
    name = models.CharField(max_length=255,default="No Subject",blank=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date = models.DateField()
    # time= models.TimeField()

    def __str__(self):
        return str(self.name)


# Students CBT Models (Models for Grading the Students)

class TestSetGroup(models.Model):
    name = models.CharField(max_length=255, default="None",blank=False)
    student = models.ForeignKey(Students_Pin_and_ID, on_delete=models.CASCADE,blank=True)
    testClass = models.ForeignKey(Class, on_delete=models.CASCADE,blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,blank=True)
    timeUsedForTest = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return str(self.name)


class TestQuestionSet(models.Model):
    testSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    testSetGroup = models.ForeignKey(TestSetGroup, on_delete=models.CASCADE)
    testTotalScore = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return str(self.testSubject.subject_name)





