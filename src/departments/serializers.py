from rest_framework import serializers

from departments.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "is_active"]
        ordering_fields = ["id", "name"]
