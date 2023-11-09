# Generated by Django 2.2 on 2023-10-29 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0002_subject'),
        ('Teachers_Portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='form_teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Classes_assigned',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Subject',
        ),
        migrations.AddField(
            model_name='attendance',
            name='Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Teachers_Portal.Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='classFormed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='classes_taught',
            field=models.ManyToManyField(related_name='assigned_classes', to='Result_portal.Class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects_taught',
            field=models.ManyToManyField(to='Result_portal.Subject'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Role',
            field=models.CharField(blank=True, choices=[('Teacher', 'Teacher'), ('FormTeacher', 'FormTeacher'), ('Admin', 'Admin')], default='Teacher', max_length=200),
        ),
        migrations.DeleteModel(
            name='FormTeachers',
        ),
    ]
