from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('General Physician', 'General Physician'),
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Orthopedic', 'Orthopedic'),
        ('Pediatrician', 'Pediatrician'),
        ('Neurologist', 'Neurologist'),
    ]
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    experience = models.IntegerField(default=1)
    fee = models.IntegerField(default=500)
    available_days = models.CharField(max_length=200, default='Mon-Sat')
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - Dr.{self.doctor.name} - {self.date}"