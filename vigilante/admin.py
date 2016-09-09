from django.contrib import admin
from vigilante.models import Store, Complaint

# Register your models here.

from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

admin.site.register(Store, LeafletGeoAdmin)
admin.site.register(Complaint)
