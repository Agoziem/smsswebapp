# Generated by Django 2.2 on 2022-12-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admission_form', '0002_auto_20221221_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, default='Admission Form', max_length=100)),
            ],
        ),
    ]
