from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='medicines'),
    path('order/<int:medicine_id>/', views.order, name='order_medicine'),
    path('success/', views.order_success, name='order_success'),
]