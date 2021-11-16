from rest_framework import viewsets

from departments.models import Department
from departments.serializers import DepartmentSerializer


class DepartmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows department to be viewed or edited.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
