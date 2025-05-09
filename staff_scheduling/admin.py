from django.contrib import admin
from .models import Staff, Schedule, TimeOffRequest

# Register models for admin interface
admin.site.register(Staff)
admin.site.register(Schedule)
admin.site.register(TimeOffRequest)