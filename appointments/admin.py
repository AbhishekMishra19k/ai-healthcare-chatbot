from django.contrib import admin
from .models import Doctor, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'experience', 'fee', 'phone', 'available_days']
    list_filter = ['specialization']
    search_fields = ['name', 'specialization']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor', 'date', 'time', 'status']
    list_filter = ['status', 'doctor']
    search_fields = ['patient_name', 'patient_phone']