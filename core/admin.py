from django.contrib import admin

from django_admin_inline_paginator.admin import TabularInlinePaginated
from mptt.admin import MPTTModelAdmin

from .models import Department, Employee


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 0
    show_change_link = True


class EmployeeInline(TabularInlinePaginated):
    model = Employee
    per_page = 100
    classes = ['collapse']
    show_change_link = True
    ordering = ('surname',)
    extra = 0


@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin):
    fields = ["parent", "name"]
    inlines = [DepartmentInline, EmployeeInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["department"]}),
        ("Full Name", {"fields": [("surname", "name", "paternal_name")]}),
        ("Info", {"fields": ["position", ("salary_amount", "employment_date")]})
    ]
    list_display = ["surname", "name", "paternal_name", "position", "salary_amount", "employment_date"]
    ordering = ('surname',)



