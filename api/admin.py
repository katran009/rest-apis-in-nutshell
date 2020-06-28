from django.contrib import admin

from api.models import Manufacturer, Shoe, ShoeColor, ShoeType

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)