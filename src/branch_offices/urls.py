from django.urls import path
from branch_offices import views as branch_offices_views


urlpatterns = [
    # Gets a collection of BranchOffice objects
    path('api/branch_offices/list', branch_offices_views.branch_offices_list),
    # Adds new BranchOffice object
    path('api/branch_offices', branch_offices_views.add_branch_office),
    # Removing or updating BranchOffice object
    path('api/branch_offices/<int:pk>', branch_offices_views.branch_offices_detail),
    ]
