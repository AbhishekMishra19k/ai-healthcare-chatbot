from django.shortcuts import render, redirect
from .models import Medicine, Order

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

def order(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total = medicine.price * quantity
        Order.objects.create(
            patient_name=request.POST['patient_name'],
            patient_phone=request.POST['patient_phone'],
            patient_address=request.POST['patient_address'],
            medicine_name=medicine.name,
            quantity=quantity,
            total_price=total,
        )
        return redirect('order_success')
    return render(request, 'medicines/order.html', {'medicine': medicine})

def order_success(request):
    return render(request, 'medicines/success.html')