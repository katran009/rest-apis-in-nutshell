from django.conf.urls import include, url
from django.urls import path

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoeViewSet
from api.views import index
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'Manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'ShoeColor', ShoeColorViewSet, basename='shoecolor')
router.register(r'ShoeType', ShoeTypeViewSet, basename='shoetype')
router.register(r'Shoe', ShoeViewSet, basename='shoe')

urlpatterns = [
    path('', index),
    url(r"^api/", include(router.urls))
]
