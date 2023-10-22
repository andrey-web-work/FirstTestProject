from rest_framework.serializers import ModelSerializer

from core.models import Employee


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["surname", "name", "paternal_name", "position", "salary_amount", "employment_date"]
