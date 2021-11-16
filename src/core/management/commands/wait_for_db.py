import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

from django.conf import settings


def write_on_stdout(handler, message):
    if not settings.IS_TESTING:
        handler.stdout.write(message)
        handler.stdout.flush()


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        write_on_stdout(self, self.style.HTTP_INFO("Check database availability"))

        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                write_on_stdout(self, self.style.WARNING("Waiting for database..."))
                time.sleep(1)

        write_on_stdout(self, self.style.SUCCESS("Database available!"))
