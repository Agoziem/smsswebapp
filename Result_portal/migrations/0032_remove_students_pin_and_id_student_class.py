# Generated by Django 2.2 on 2024-11-28 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0031_auto_20241128_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students_pin_and_id',
            name='student_class',
        ),
    ]
