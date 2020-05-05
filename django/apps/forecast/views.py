import json
import os
import pandas as pd
import requests
from datetime import datetime
from dateutil.tz import gettz
from rest_framework.response import Response
from rest_framework.views import APIView
from typing import Any, Dict

from .models import Forecast
from region.models import City


class ForecastView(APIView):

    def _get_forecast_json(self, city_id: str):
        city = City.objects.get(id=city_id)
        api_key = os.environ['DARKSKY_API_KEY']
        exclude = (
            'currently',
            'minutely',
            'hourly',
            'alerts',
            'flags',
        )

        exclude_str = ','.join(exclude)
        url = f'https://api.darksky.net/forecast/{api_key}/{city.lat},{city.lon}?units=auto&exclude={exclude_str}'
        res = requests.get(url)

        response_data = dict()  # type: Dict[str, Any]

        forecast_data = res.json()['daily']['data']
        fields = [
            'date',
            'precipProbability',
            'temperatureHigh',
            'temperatureLow',
        ]
        forecast_df = pd.json_normalize(forecast_data)
        forecast_df['date'] = (
            forecast_df['time']
            .map(lambda x: datetime.fromtimestamp(x).date().isoformat())
        )
        response_data['forecast'] = forecast_df[fields].to_dict('records')

        response_data['provider'] = {
            'message': 'Powered by Dark Sky',
            'link': 'https://darksky.net/poweredby/',
        }

        return json.dumps(response_data)

    def get(self, request, city_id):
        try:
            forecast = Forecast.objects.get(city=city_id)
            today = datetime.now(tz=gettz(os.environ['TZ'])).date()
            if forecast.date != today:
                forecast.date = today
                forecast.forecast_json = self._get_forecast_json(city_id)
                forecast.save()
        except Forecast.DoesNotExist:
            forecast = Forecast(
                city=City.objects.get(id=city_id),
                forecast_json=self._get_forecast_json(city_id),
            )
            forecast.save()
        return Response(json.loads(forecast.forecast_json))
