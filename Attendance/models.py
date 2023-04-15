from django.db import models
from django.contrib.auth.models import User
from Result_portal.models import Students_Pin_and_ID
from Home.models import FormTeachers
from django.utils import timezone
from datetime import timedelta



class Attendance(models.Model):
    student = models.ForeignKey(Students_Pin_and_ID, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    form_teacher = models.ForeignKey(FormTeachers, on_delete=models.CASCADE, blank=True, null=True)
    is_present = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        unique_together = ['student', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} ({self.date}): {'Present' if self.is_present else 'Absent'}"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, using=None):
        super().delete(using=using)

    




