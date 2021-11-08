from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.name
