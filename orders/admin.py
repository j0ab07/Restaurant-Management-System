from django.contrib import admin
from .models import Menu, Order, OrderItem

# Register models for admin interface
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)