from django.db import models
from django.contrib import admin
from branch_offices.models import Branch_Offices


# Register your models here.
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    branch_office_id = models.ForeignKey(Branch_Offices,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class EmployeesHours(models.Model):
    employees_hours_id = models.IntegerField()
    time_period = models.DateField()
    value = models.IntegerField()
    employee_id = models.ForeignKey(Employees,on_delete=models.CASCADE)

    def get_EmployeesHours(year, author):
        url = 'http://api.example.com/books'
        params = {'year': year, 'author': author}
        r = requests.get(url, params=params)