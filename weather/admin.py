from django.contrib import admin
from .models import City
# Register your models here.
admin.site.site_header = 'Weather App'
admin.site.title = 'Weather App'

admin.site.register(City)