from django.contrib import admin
from .models import Summary

admin.site.register(Summary)

admin.site.site_header = "Symbiotic Devices Admin"
admin.site.site_title = "Symbiotic Devices"
admin.site.index_title = "Welcome to the Symbiotic Devices Portal"

# Register your models here.
