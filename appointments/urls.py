from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='appointments'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.success, name='appointment_success'),
]