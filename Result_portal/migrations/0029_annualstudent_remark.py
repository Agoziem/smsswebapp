# Generated by Django 2.2 on 2024-08-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0028_annualstudent_verdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualstudent',
            name='Remark',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
    ]