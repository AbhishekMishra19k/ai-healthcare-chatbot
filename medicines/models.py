from django.db import models

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

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
    ]
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15)
    patient_address = models.TextField()
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.medicine_name}"