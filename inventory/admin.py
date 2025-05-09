from django.contrib import admin
from .models import Stock, MenuIngredients

# Register models for admin interface
admin.site.register(Stock)
admin.site.register(MenuIngredients)