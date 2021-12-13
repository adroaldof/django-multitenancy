from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from tenants.models import Domain, Tenant

TENANTS_URL = "/tenants/"
DOMAIN = "testserver"


payload_with_domains = {
    "schema_name": "second",
    "name": "Second Tenant",
    "sub_domains": ["second", "segundo"],
}


class PublicTenantsApiTests(APITestCase):
    def setUp(self):
        """
        Create public root tenant to use in tests and assign it to `testserver`
        domain to match with Django's test server
        """
        root_tenant = Tenant(schema_name="public", name="Root")
        root_tenant.save()
        root_domain = Domain(domain=DOMAIN, tenant=root_tenant)
        root_domain.save()

        self.client = APIClient()

    def test_get_tenants(self):
        response = self.client.get(TENANTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["content-type"], "application/json")

    def test_create_tenant_without_domains(self):
        payload_without_domains = {
            key: payload_with_domains[key] for key in ["schema_name", "name"]
        }

        response = self.client.post(TENANTS_URL, payload_without_domains)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Tenant.objects.filter(name=payload_without_domains["name"]).exists()
        )

    def test_create_tenant_with_domains(self):
        response = self.client.post(TENANTS_URL, payload_with_domains)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Domain.objects.filter(
                domain=f"{payload_with_domains['sub_domains'][0]}.{DOMAIN}"
            ).exists()
        )
        self.assertTrue(
            Domain.objects.filter(
                domain=f"{payload_with_domains['sub_domains'][1]}.{DOMAIN}"
            ).exists()
        )

    def test_get_tenants_domains(self):
        created_tenant = self.client.post(TENANTS_URL, payload_with_domains)
        tenant_domains_url = f"{TENANTS_URL}{created_tenant.data['id']}/domains/"
        tenant_domains = self.client.get(tenant_domains_url)

        self.assertEqual(tenant_domains.status_code, status.HTTP_200_OK)

        self.assertEquals(
            tenant_domains.data["count"],
            len(payload_with_domains["sub_domains"]),
        )
