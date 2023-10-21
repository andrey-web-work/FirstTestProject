from datetime import date
from random import random, randint, choice

from django.db import migrations
from django.utils.crypto import get_random_string

from core.models import Department, Employee


def create_departments(apps, schema_editor):
    total_departments = 0

    while total_departments < 25:
        department = None

        for level in range(5):
            departments = []
            main_department = department

            if main_department:
                departments_random = 3
            else:
                departments_random = 1

            for dep in range(departments_random):
                if total_departments < 25:
                    department_name = get_random_string(
                        length=randint(8, 16),
                        allowed_chars="abcdefghijklmnopqrstuvwxyz"
                    ).title()

                    department = Department(
                        name=department_name,
                        parent=main_department,
                        lft=0,
                        rght=0,
                        tree_id=0,
                        level=0
                    )

                    departments.append(department)

                    total_departments += 1

                else:
                    break

            Department.objects.bulk_create(departments)

    Department.objects.rebuild()


def create_employee(apps, schema_editor):
    employees = []

    departments_ids = Department.objects.values_list('id', flat=True)

    start_date = date(2012, 10, 1)
    end_date = date.today()

    for emp in range(50000):
        department_id = choice(departments_ids)

        random_date = start_date + (end_date - start_date) * random()

        employee = Employee(
            department_id=department_id,
            surname=get_random_string(
                length=randint(8, 16),
                allowed_chars="abcdefghijklmnopqrstuvwxyz"
            ).title(),
            name=get_random_string(
                length=randint(8, 16),
                allowed_chars="abcdefghijklmnopqrstuvwxyz"
            ).title(),
            paternal_name=get_random_string(
                length=randint(8, 16),
                allowed_chars="abcdefghijklmnopqrstuvwxyz"
            ).title(),
            position=get_random_string(
                length=randint(8, 16),
                allowed_chars="abcdefghijklmnopqrstuvwxyz"
            ).title(),
            salary_amount=randint(10000, 200000),
            employment_date=random_date,
        )

        employees.append(employee)

    Employee.objects.bulk_create(employees)


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_departments),
        migrations.RunPython(create_employee)
    ]
