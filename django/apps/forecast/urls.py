from django.urls import path

from .views import ForecastView


urlpatterns = [
    path('<str:city_id>/', ForecastView.as_view()),
]
