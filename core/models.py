from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name=_("main department")
    )
    name = models.CharField(max_length=50, verbose_name=_("department name"))

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "parent")
        verbose_name = _("department")
        verbose_name_plural = _("departments")

    class MPTTMeta:
        order_insertion_by = ['name']


class Employee(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name=_("department")
    )
    surname = models.CharField(max_length=50, verbose_name=_("surname"))
    name = models.CharField(max_length=50, verbose_name=_("name"))
    paternal_name = models.CharField(max_length=50, blank=True, verbose_name=_("paternal name"))
    position = models.CharField(max_length=50, blank=True, verbose_name=_("position"))
    salary_amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=0,
        validators=[validators.MinValueValidator(0)],
        verbose_name=_("salary amount")
    )
    employment_date = models.DateField(default=timezone.now, verbose_name=_("employment date"))

    def __str__(self):
        return f'{self.surname} {self.name} {self.paternal_name}'

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")
