import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from appointments.models import Doctor
from faker import Faker
import random

fake = Faker('en_IN')

Doctor.objects.all().delete()
print("Purane doctors delete ho gaye...")

specializations = [
    'General Physician', 'Cardiologist', 'Dermatologist',
    'Orthopedic', 'Pediatrician', 'Neurologist',
    'Gynecologist', 'Psychiatrist', 'Ophthalmologist',
    'ENT Specialist', 'Urologist', 'Gastroenterologist',
]

available_days_list = ['Mon-Sat', 'Mon-Fri', 'Tue-Sun', 'Mon-Wed-Fri', 'Tue-Thu-Sat']

fees = {
    'General Physician': (400, 600),
    'Cardiologist': (1000, 1500),
    'Dermatologist': (700, 1000),
    'Orthopedic': (800, 1200),
    'Pediatrician': (500, 800),
    'Neurologist': (1200, 1800),
    'Gynecologist': (600, 1000),
    'Psychiatrist': (800, 1200),
    'Ophthalmologist': (600, 900),
    'ENT Specialist': (500, 800),
    'Urologist': (900, 1300),
    'Gastroenterologist': (1000, 1500),
}

for i in range(1000):
    spec = random.choice(specializations)
    fee_range = fees[spec]
    Doctor.objects.create(
        name=fake.name().replace('Dr. ', ''),
        specialization=spec,
        phone=fake.numerify('9#########'),
        email=fake.email(),
        experience=random.randint(1, 30),
        fee=random.randint(fee_range[0], fee_range[1]),
        available_days=random.choice(available_days_list),
    )
    if (i+1) % 100 == 0:
        print(f"✅ {i+1} doctors added...")

print(f"\n🎉 Total {Doctor.objects.count()} doctors added!")