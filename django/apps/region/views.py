# coding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import City, Subdivision
from .serializer import CitySerializer, SubdivisionSerializer


class SubdivisionViewSet(ReadOnlyModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('subdivision',)
