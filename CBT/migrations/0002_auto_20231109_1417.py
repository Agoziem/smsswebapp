# Generated by Django 2.2 on 2023-11-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionset',
            name='ExamClass',
            field=models.ManyToManyField(blank=True, null=True, to='Result_portal.Class'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='questions',
            field=models.ManyToManyField(blank=True, null=True, to='CBT.Question'),
        ),
    ]
