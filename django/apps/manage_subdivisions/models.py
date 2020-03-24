from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Subdivision(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=16)
    local_name = models.CharField(max_length=16)

class City(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    subdivision = models.ForeignKey(Subdivision, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    local_name = models.CharField(max_length=64)
    lat = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    lon = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])

