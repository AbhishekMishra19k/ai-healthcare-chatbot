from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Medicine, Order


def index(request):
    category = request.GET.get('category', '')
    if category:
        medicines = Medicine.objects.filter(category=category)
    else:
        medicines = Medicine.objects.all()
    categories = Medicine.CATEGORY_CHOICES
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    return render(request, 'medicines/index.html', {
        'medicines': medicines,
        'categories': categories,
        'selected_category': category,
        'cart_count': cart_count,
    })


def add_to_cart(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    cart = request.session.get('cart', {})
    key = str(medicine_id)
    if key in cart:
        cart[key]['quantity'] += 1
    else:
        cart[key] = {
            'name': medicine.name,
            'price': medicine.price,
            'quantity': 1,
        }
    request.session['cart'] = cart
    messages.success(request, f'{medicine.name} cart mein add ho gaya!')
    return redirect('medicines')


def remove_from_cart(request, medicine_id):
    cart = request.session.get('cart', {})
    key = str(medicine_id)
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for med_id, item in cart.items():
        subtotal = item['price'] * item['quantity']
        total += subtotal
        cart_items.append({
            'id': med_id,
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'subtotal': subtotal,
        })
    return render(request, 'medicines/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Cart khaali hai!')
        return redirect('medicines')

    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_phone = request.POST['patient_phone']
        patient_address = request.POST['patient_address']
        total = 0
        medicine_names = []

        for med_id, item in cart.items():
            subtotal = item['price'] * item['quantity']
            total += subtotal
            medicine_names.append(f"{item['name']} x{item['quantity']}")
            Order.objects.create(
                patient_name=patient_name,
                patient_phone=patient_phone,
                patient_address=patient_address,
                medicine_name=item['name'],
                quantity=item['quantity'],
                total_price=subtotal,
            )

        medicines_list = '\n'.join(medicine_names)
        send_mail(
            subject='Order Confirmed — AIHealthCare',
            message=f'''Namaste {patient_name}!

Aapka order confirm ho gaya hai.

Medicines:
{medicines_list}

Total: Rs.{total}
Delivery Address: {patient_address}

AIHealthCare Team''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.POST.get('patient_email', settings.ADMIN_EMAIL)],
            fail_silently=True,
        )

        request.session['cart'] = {}
        return redirect('order_success')

    cart_items = []
    total = 0
    for med_id, item in cart.items():
        subtotal = item['price'] * item['quantity']
        total += subtotal
        cart_items.append({
            'id': med_id,
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'subtotal': subtotal,
        })
    return render(request, 'medicines/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def order_success(request):
    return render(request, 'medicines/success.html')