from django.urls import path

from .views import EmployeeListApi


urlpatterns = [
    path('employees/department/<int:pk>/', EmployeeListApi.as_view())
]