from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class WaitForDBCommandTests(TestCase):
    django_connection_handler = "django.db.utils.ConnectionHandler.__getitem__"

    def test_when_database_is_already_available(self):
        with patch(self.django_connection_handler) as connection_handler:
            connection_handler.return_value = True
            call_command("wait_for_db")
            self.assertEqual(connection_handler.call_count, 1)

    @patch("time.sleep", return_value=True)
    def test_when_need_to_wait_database_to_be_ready(self, ts):
        with patch(self.django_connection_handler) as connection_handler:
            connection_handler.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            self.assertEqual(connection_handler.call_count, 6)
