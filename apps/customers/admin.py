from django.contrib import admin

from .models import Company, Customer, Location, Person

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Person)
