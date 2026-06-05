from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Medicine, Order, OrderItem, Cart, CartItem


def _get_cart_and_items(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        return cart, [], 0, 0
    cart_items = list(cart.items.select_related('medicine').all())
    cart_count = sum(i.quantity for i in cart_items)
    cart_total = sum(i.medicine.price * i.quantity for i in cart_items)
    return cart, cart_items, cart_count, cart_total


def index(request):
    category = request.GET.get('category', '')
    if category:
        medicines = Medicine.objects.filter(category=category)
    else:
        medicines = Medicine.objects.all()
    categories = Medicine.CATEGORY_CHOICES
    return render(request, 'medicines/index.html', {
        'medicines': medicines,
        'categories': categories,
        'selected_category': category
    })

@login_required
@transaction.atomic
def add_to_cart(request, medicine_id):
    medicine = Medicine.objects.select_for_update().get(id=medicine_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, medicine=medicine, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('medicines_cart')

@login_required
def cart_view(request):
    cart, cart_items, _, cart_total = _get_cart_and_items(request)
    return render(request, 'medicines/cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })


@login_required
@transaction.atomic
def checkout(request):
    cart, cart_items, cart_count, cart_total = _get_cart_and_items(request)

    if not cart or not cart.items.exists():
        return redirect('medicines_cart')

    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_phone = request.POST['patient_phone']
        patient_address = request.POST['patient_address']

        cart_items = list(cart.items.select_related('medicine').all())
        total_price = sum(item.medicine.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            patient_name=patient_name,
            patient_phone=patient_phone,
            patient_address=patient_address,
            total_price=total_price,
            status='Pending',
            medicine_name='',
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                medicine=item.medicine,
                medicine_name=item.medicine.name,
                quantity=item.quantity,
                price=item.medicine.price,
                total_price=item.medicine.price * item.quantity,
            )

        # clear cart
        cart.items.all().delete()

        return render(request, 'medicines/cart_success.html', {'order': order})

    # GET
    return render(request, 'medicines/checkout.html', {

        'cart_items': cart_items,
        'cart_count': cart_count,
        'cart_total': cart_total,
    })


# Backward-compatible single-medicine order flow (optional). Kept as-is if templates/routes exist.
def order(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total = medicine.price * quantity
        # create header + one item for the old flow
        order_obj = Order.objects.create(
            patient_name=request.POST['patient_name'],
            patient_phone=request.POST['patient_phone'],
            patient_address=request.POST['patient_address'],
            medicine_name=medicine.name,
            total_price=total,
            status='Pending',
        )

        OrderItem.objects.create(
            order=order_obj,
            medicine=medicine,
            medicine_name=medicine.name,
            quantity=quantity,
            price=medicine.price,
            total_price=total,
        )
        return redirect('order_success')
    return render(request, 'medicines/order.html', {'medicine': medicine})

def order_success(request):
    return render(request, 'medicines/success.html')



