from rest_framework import viewsets, generics

from tenants.models import Domain, Tenant
from tenants.serializers import TenantSerializer, TenantDomainsSerializer


class TenantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tenants to be viewed or edited
    """

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantDomainsView(generics.ListAPIView):
    """
    API endpoint that allows tenants domains to be viewed
    """

    serializer_class = TenantDomainsSerializer

    def get_queryset(self):
        return Domain.objects.filter(tenant_id=self.kwargs["pk"])
