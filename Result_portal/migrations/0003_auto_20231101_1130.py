# Generated by Django 2.2 on 2023-11-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_pin_and_id',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Class'),
        ),
    ]
