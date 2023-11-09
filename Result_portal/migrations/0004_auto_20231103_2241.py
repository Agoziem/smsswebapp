# Generated by Django 2.2 on 2023-11-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0003_auto_20231101_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Result_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalScore', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Totalnumber', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Average', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Position', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Students_Pin_and_ID')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, max_length=100)),
                ('academicsession', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Result_portal.AcademicSession')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RenameField(
            model_name='annualresult',
            old_name='FirstTerm',
            new_name='FirstTermTotal',
        ),
        migrations.RenameField(
            model_name='annualresult',
            old_name='SN',
            new_name='SecondTermTotal',
        ),
        migrations.RenameField(
            model_name='annualresult',
            old_name='SecondTerm',
            new_name='ThirdTermTotal',
        ),
        migrations.RemoveField(
            model_name='annualresult',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='annualresult',
            name='Student_id',
        ),
        migrations.RemoveField(
            model_name='annualresult',
            name='ThirdTerm',
        ),
        migrations.RemoveField(
            model_name='annualresult',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='annualstudent',
            name='Academicsession',
        ),
        migrations.RemoveField(
            model_name='annualstudent',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='annualstudent',
            name='Student_id',
        ),
        migrations.RemoveField(
            model_name='annualstudent',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='result',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='result',
            name='SN',
        ),
        migrations.RemoveField(
            model_name='result',
            name='Student_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student_name',
        ),
        migrations.AddField(
            model_name='annualstudent',
            name='Student_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Students_Pin_and_ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annualresult',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Subject'),
        ),
        migrations.AlterField(
            model_name='annualstudent',
            name='Term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Term'),
        ),
        migrations.AlterField(
            model_name='result',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Subject'),
        ),
        migrations.AddField(
            model_name='student_result_data',
            name='Term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Term'),
        ),
        migrations.AddField(
            model_name='annualresult',
            name='students_result_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Student_Result_Data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='students_result_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Result_portal.Student_Result_Data'),
            preserve_default=False,
        ),
    ]