from django.contrib import admin
from .models import Table, Reservation

# Register models for admin interface
admin.site.register(Table)
admin.site.register(Reservation)