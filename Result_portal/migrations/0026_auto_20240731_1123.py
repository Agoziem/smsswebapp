# Generated by Django 2.2 on 2024-07-31 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0025_auto_20240725_0518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualresult',
            old_name='students_result_data',
            new_name='Student_name',
        ),
    ]
