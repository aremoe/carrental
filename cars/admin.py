from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day', 'available')
    list_filter = ('available', 'year', 'brand')
    search_fields = ('brand', 'model')