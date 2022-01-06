from django.contrib import admin

from .models import CommodityOrder, Payment

admin.site.register(CommodityOrder)
admin.site.register(Payment)

