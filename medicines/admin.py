from django.contrib import admin

from .models import Medicine, Order, OrderItem


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    search_fields = ['name', 'category']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'total_price', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['patient_name', 'patient_phone']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'medicine_name', 'quantity', 'price', 'total_price', 'created_at']
    list_filter = ['created_at']

