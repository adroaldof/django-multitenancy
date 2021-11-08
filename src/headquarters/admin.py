from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from headquarters.models import Headquarter


@admin.register(Headquarter)
class HeadquarterAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
