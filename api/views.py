from rest_framework.generics import ListAPIView

from core.models import Employee

from .serializers import EmployeesSerializer


class EmployeeListApi(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        return super().get_queryset().filter(department_id=self.kwargs['pk'])
