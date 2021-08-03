from django.contrib import admin
from .models import Trip, Destination, Resort

# Register your models here.
admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Resort)