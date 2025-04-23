from django.contrib import admin
from .models import Staff, Schedule, TimeOffRequest

admin.site.register(Staff)
admin.site.register(Schedule)
admin.site.register(TimeOffRequest)