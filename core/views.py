from django.views.generic import ListView

from .models import Department


class DepartmentListView(ListView):
    model = Department

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["departments_list"] = Department.objects.all().prefetch_related("employees")

        return context