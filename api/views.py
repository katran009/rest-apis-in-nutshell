from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer
from api.models import Manufacturer, ShoeColor, ShoeType, Shoe

# Create your views here.
def index(request):
    return render(request, 'index.html')


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'shoe_color'
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'shoe_type'
    queryset = ShoeType.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    queryset = Shoe.objects.all()