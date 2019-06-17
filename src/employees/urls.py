from django.urls import path
from employees import views as employees_views


urlpatterns = [
    # Showing all employees
    path('api/employees/all', employees_views.employees_list_all),
    # Adding employee
    path('api/employees', employees_views.add_employee),
    # Gets a collection of employee objects by branchOfficeId
    path('api/employees/list/<int:branchOfficeId>', employees_views.employees_list),
    # Removing or updating employee
    path('api/employees/<int:pk>', employees_views.employees_detail),
    # To show employees and hours worked by each of them
    path('api/employee_hours/list', employees_views.employees_hours),
    path('api/salaries', employees_views.employees_salaries),
    path('api/branch_offices/<int:branchOfficeId>/employees/<int:emp_id>/employee_hours', employees_views.employees_hours_per_BO),
]
