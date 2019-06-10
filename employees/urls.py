from django.urls import path
from employees import views as employees_views


urlpatterns = [
    path('employees/', employees_views.employees_list),
    path('employees/<int:pk>/', employees_views.employees_detail),
]