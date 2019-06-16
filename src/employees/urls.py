from django.urls import path
from employees import views as employees_views


urlpatterns = [
    path('api/employees/', employees_views.employees_list),
    path('api/employees/<int:pk>/', employees_views.employees_detail),
    path('api/employee_hours/list/', employees_views.employees_hours),
    path('api/salaries/', employees_views.employees_salaries),
]