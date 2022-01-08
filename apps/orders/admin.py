from django.contrib import admin

from .models import ProductOrder, Payment

admin.site.register(ProductOrder)
admin.site.register(Payment)

