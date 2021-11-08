from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Headquarter(TenantMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
