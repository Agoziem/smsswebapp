# Generated by Django 2.2 on 2023-01-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20221230_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='Flier',
            field=models.ImageField(blank=True, upload_to='assets'),
        ),
    ]