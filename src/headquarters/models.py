from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Headquarter(TenantMixin):
    """
    The model responsible for the tenants
    """

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
