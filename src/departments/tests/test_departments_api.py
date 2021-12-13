from django.urls import reverse

from rest_framework import status

from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient


DEPARTMENTS_URL = reverse("departments:department-list")


class PublicDepartmentsApiTests(TenantTestCase):
    def setUp(self):
        self.client = TenantClient(self.tenant)

    def test_get_all_tenants(self):
        response = self.client.get(DEPARTMENTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
