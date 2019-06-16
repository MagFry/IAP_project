from django.db import models
from django.contrib import admin



# Register your models here.
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    pay = models.FloatField()
    branch_office_id = models.IntegerField()
    isManager = models.BooleanField()

    def __str__(self):
        return self.first_name

class EmployeesHours(models.Model):
    employees_hours_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    value = models.IntegerField()
    employee_id = models.IntegerField()

    def __int__(self):
        return self.employee_id

class EmployeesSalaries(models.Model):
    employee_salary_id = models.AutoField(primary_key=True)
    salary = models.FloatField()