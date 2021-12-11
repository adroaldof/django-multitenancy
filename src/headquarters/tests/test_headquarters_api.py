from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from headquarters.models import Domain, Headquarter

HEADQUARTERS_URL = "/headquarters/"
DOMAIN = "testserver"


class PublicHeadquartersApiTests(APITestCase):
    def setUp(self):
        """
        Create public root tenant to use in tests and assign it to `testserver`
        domain to match with Django's test server
        """
        root_tenant = Headquarter(schema_name="public", name="Root")
        root_tenant.save()
        root_domain = Domain(domain=DOMAIN, tenant=root_tenant)
        root_domain.save()

        self.client = APIClient()

    def get_headquarters(self):
        response = self.client.get(HEADQUARTERS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_headquarter_without_domains(self):
        payload_without_domains = {
            "schema_name": "first",
            "name": "First Tenant",
        }

        response = self.client.post(HEADQUARTERS_URL, payload_without_domains)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Headquarter.objects.filter(name=payload_without_domains["name"]).exists()
        )

    def test_create_headquarter_with_domains(self):
        sub_domains = ["second", "segundo"]
        payload_with_domais = {
            "schema_name": "second",
            "name": "Second Tenant",
            "sub_domains": sub_domains,
        }

        response = self.client.post(HEADQUARTERS_URL, payload_with_domais)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Domain.objects.filter(domain=f"{sub_domains[0]}.{DOMAIN}").exists()
        )
        self.assertTrue(
            Domain.objects.filter(domain=f"{sub_domains[1]}.{DOMAIN}").exists()
        )
