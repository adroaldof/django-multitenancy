from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from headquarters.models import Domain, Headquarter
from headquarters.serializers import HeadquarterSerializer


class HeadquarterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows headquarters to be viewed or edited.
    """

    queryset = Headquarter.objects.all()
    serializer_class = HeadquarterSerializer
