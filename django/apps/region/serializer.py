# coding: utf-8
from rest_framework.serializers import ModelSerializer

from .models import City, Subdivision


class SubdivisionSerializer(ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ('id', 'name', 'local_name')


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'local_name', 'subdivision')
