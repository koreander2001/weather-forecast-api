from django.db import models

from region import models as region_models


class Forecast(models.Model):
    city = models.OneToOneField(
        region_models.City, related_name='city', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    forecast_json = models.TextField()
