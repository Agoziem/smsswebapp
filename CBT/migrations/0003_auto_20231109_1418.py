# Generated by Django 2.2 on 2023-11-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBT', '0002_auto_20231109_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionset',
            name='ExamClass',
            field=models.ManyToManyField(blank=True, to='Result_portal.Class'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='questions',
            field=models.ManyToManyField(blank=True, to='CBT.Question'),
        ),
    ]
