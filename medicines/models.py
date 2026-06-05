from django.db import models
from django.conf import settings


class Medicine(models.Model):
    CATEGORY_CHOICES = [
        ('Fever', 'Fever'),
        ('Cold & Cough', 'Cold & Cough'),
        ('Stomach', 'Stomach'),
        ('Pain Relief', 'Pain Relief'),
        ('Vitamins', 'Vitamins'),
        ('Antibiotics', 'Antibiotics'),
        ('Skin Care', 'Skin Care'),
        ('General', 'General'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.IntegerField(default=50)
    description = models.TextField()
    dosage = models.CharField(max_length=200, default='As directed by physician')
    stock = models.IntegerField(default=100)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category}"





class Cart(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='cart',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id}" 


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('cart', 'medicine'),)

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}" 


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
    ]

    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15)
    patient_address = models.TextField()

    # Backward-compat: keep field, but now order has multiple items.
    medicine_name = models.CharField(max_length=200, default='')

    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.medicine_name}" 


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    medicine = models.ForeignKey(
        Medicine,
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine_name} ({self.quantity})"

