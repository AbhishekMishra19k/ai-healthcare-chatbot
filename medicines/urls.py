from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='medicines'),

    # Single-medicine (legacy)
    path('order/<int:medicine_id>/', views.order, name='order_medicine'),
    path('success/', views.order_success, name='order_success'),

    # Cart + multi-medicine checkout
    path('cart/', views.cart_view, name='medicines_cart'),
    path('add-to-cart/<int:medicine_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='medicines_checkout'),
]

