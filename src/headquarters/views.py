from rest_framework import viewsets

from headquarters.models import Headquarter
from headquarters.serializers import HeadquarterSerializer


class HeadquartersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows headquarters to be viewed or edited.
    """

    queryset = Headquarter.objects.all()
    serializer_class = HeadquarterSerializer
