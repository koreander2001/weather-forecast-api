# coding: utf-8
from rest_framework import routers

from .views import CityViewSet, SubdivisionViewSet


router = routers.DefaultRouter()
router.register(r'subdivisions', SubdivisionViewSet)
router.register(r'cities', CityViewSet)
urlpatterns = router.urls
