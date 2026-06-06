from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='medicines'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:medicine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:medicine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
]