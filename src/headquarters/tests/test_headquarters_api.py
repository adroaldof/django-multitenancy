import json

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from headquarters.models import Headquarter, Domain


HEADQUARTERS_URL = "/headquarters/"


class PublicHeadquartersApiTests(TestCase):
    def setUp(self):
        """
        Create public root tenant to use in tests and assign it to `testserver`
        domain to match with Django's test server
        """
        root_tenant = Headquarter(schema_name="public", name="Root")
        root_tenant.save()
        root_domain = Domain(domain="testserver", tenant=root_tenant)
        root_domain.save()

        self.client = APIClient()

    def test_get_headquarters(self):
        response = self.client.get(HEADQUARTERS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
