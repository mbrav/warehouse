from django.contrib import admin

from .models import Commodity, CommodityCategory, Stock

admin.site.register(Commodity)
admin.site.register(CommodityCategory)
admin.site.register(Stock)

