from django.urls import path
from branch_offices import views as branch_offices_views


urlpatterns = [
    # Gets a collection of BranchOffice objects
    path('api/branch_offices/list', branch_offices_views.branch_offices_list),
    path('api/branch_offices/<int:pk>', branch_offices_views.branch_offices_detail),
    ]
