# Generated by Django 2.2.2 on 2019-06-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('pay', models.FloatField()),
                ('branch_office_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesHours',
            fields=[
                ('employees_hours_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('value', models.IntegerField()),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesSalaries',
            fields=[
                ('employee_salary_id', models.AutoField(primary_key=True, serialize=False)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
