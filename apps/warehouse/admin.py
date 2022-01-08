from django.contrib import admin

from .models import Product, ProductCategory, Stock

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Stock)
