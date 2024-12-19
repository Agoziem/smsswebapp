# Generated by Django 2.2 on 2024-11-28 06:47

from django.db import migrations

def migrate_student_classes(apps, schema_editor):
    # Get models
    Students_Pin_and_ID = apps.get_model('Result_portal', 'Students_Pin_and_ID')
    StudentClassEnrollment = apps.get_model('Result_portal', 'StudentClassEnrollment')
    AcademicSession = apps.get_model('Result_portal', 'AcademicSession')
    Class = apps.get_model('Result_portal', 'Class')

    # Create a default session if none exist
    session, _ = AcademicSession.objects.get_or_create(session="2023/2024")

    # Iterate through all students and migrate their class data
    for student in Students_Pin_and_ID.objects.all():
        if student.student_class:
            StudentClassEnrollment.objects.create(
                student=student,
                student_class=student.student_class,
                academic_session=session,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0030_studentclassenrollment'),
    ]

    operations = [
        migrations.RunPython(migrate_student_classes),
    ]