from django.contrib import admin
from .models import Medicine, Order

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    search_fields = ['name', 'category']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'medicine_name', 'quantity', 'total_price', 'status']
    list_filter = ['status']