from django.urls import path, include

from rest_framework import routers

from tenants.views import TenantsViewSet, TenantDomainsView

router = routers.DefaultRouter()
router.register("", TenantsViewSet)

app_name = "tenants"

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/domains/", TenantDomainsView.as_view()),
]
