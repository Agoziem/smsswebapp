# Generated by Django 2.2 on 2023-11-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0020_subject_subject_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_result_data',
            name='Remark',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
    ]