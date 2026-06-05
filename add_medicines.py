import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from medicines.models import Medicine

Medicine.objects.all().delete()
print("Purani medicines delete ho gayi...")

medicines = [
    {"name": "Amoxicillin 500mg", "category": "Antibiotics", "price": 35, "description": "Bacterial infections ke liye", "dosage": "1 tablet 3 times daily", "stock": 90},
    {"name": "Azithromycin 250mg", "category": "Antibiotics", "price": 45, "description": "Respiratory infections ke liye", "dosage": "1 tablet daily for 3 days", "stock": 80},
    {"name": "Ciprofloxacin 500mg", "category": "Antibiotics", "price": 40, "description": "Urinary infections ke liye", "dosage": "1 tablet twice daily", "stock": 70},
    {"name": "Paracetamol 650mg", "category": "Pain Relief", "price": 25, "description": "Fever aur pain ke liye", "dosage": "1 tablet every 6 hours", "stock": 120},
    {"name": "Ibuprofen 400mg", "category": "Pain Relief", "price": 30, "description": "Pain aur inflammation ke liye", "dosage": "1 tablet 3 times daily after food", "stock": 110},
    {"name": "Diclofenac 50mg", "category": "Pain Relief", "price": 28, "description": "Joint pain ke liye", "dosage": "1 tablet twice daily", "stock": 90},
    {"name": "Cetirizine 10mg", "category": "Allergy", "price": 20, "description": "Allergy relief ke liye", "dosage": "1 tablet at night", "stock": 140},
    {"name": "Loratadine 10mg", "category": "Allergy", "price": 22, "description": "Hay fever ke liye", "dosage": "1 tablet daily", "stock": 130},
    {"name": "Omeprazole 20mg", "category": "Gastric", "price": 27, "description": "Acidity ke liye", "dosage": "1 capsule before breakfast", "stock": 150},
    {"name": "Pantoprazole 40mg", "category": "Gastric", "price": 30, "description": "Acid reflux ke liye", "dosage": "1 tablet before meal", "stock": 140},
    {"name": "Salbutamol Inhaler", "category": "Respiratory", "price": 60, "description": "Asthma relief ke liye", "dosage": "2 puffs as needed", "stock": 50},
    {"name": "Montelukast 10mg", "category": "Respiratory", "price": 40, "description": "Asthma prevention ke liye", "dosage": "1 tablet at night", "stock": 80},
    {"name": "Metformin 500mg", "category": "Diabetes", "price": 30, "description": "Blood sugar control ke liye", "dosage": "1 tablet twice daily with food", "stock": 150},
    {"name": "Glimepiride 2mg", "category": "Diabetes", "price": 28, "description": "Type 2 diabetes ke liye", "dosage": "1 tablet before breakfast", "stock": 140},
    {"name": "Amlodipine 5mg", "category": "Blood Pressure", "price": 25, "description": "Hypertension ke liye", "dosage": "1 tablet daily", "stock": 160},
    {"name": "Losartan 50mg", "category": "Blood Pressure", "price": 28, "description": "BP control ke liye", "dosage": "1 tablet daily", "stock": 150},
    {"name": "Atorvastatin 10mg", "category": "Cholesterol", "price": 35, "description": "Cholesterol kam karne ke liye", "dosage": "1 tablet at night", "stock": 140},
    {"name": "Multivitamin Tablets", "category": "Vitamins", "price": 20, "description": "Nutritional support ke liye", "dosage": "1 tablet daily after food", "stock": 200},
    {"name": "Vitamin C 500mg", "category": "Vitamins", "price": 18, "description": "Immunity boost ke liye", "dosage": "1 tablet daily", "stock": 180},
    {"name": "Vitamin D3 1000IU", "category": "Vitamins", "price": 22, "description": "Bone health ke liye", "dosage": "1 tablet daily with food", "stock": 170},
    {"name": "Hydrocortisone Cream", "category": "Skin Care", "price": 15, "description": "Itching aur rash ke liye", "dosage": "Apply twice daily on affected area", "stock": 120},
    {"name": "Clotrimazole Cream", "category": "Skin Care", "price": 18, "description": "Fungal infection ke liye", "dosage": "Apply twice daily", "stock": 110},
    {"name": "Oral Rehydration Salt", "category": "General", "price": 10, "description": "Dehydration ke liye", "dosage": "1 sachet in 1 liter water", "stock": 200},
    {"name": "Ambroxol 30mg", "category": "Cold & Cough", "price": 25, "description": "Cough relief ke liye", "dosage": "1 tablet 3 times daily", "stock": 110},
    {"name": "Fluconazole 150mg", "category": "Antibiotics", "price": 35, "description": "Fungal infection ke liye", "dosage": "1 tablet single dose", "stock": 100},
    {"name": "Sertraline 50mg", "category": "General", "price": 55, "description": "Depression ke liye", "dosage": "1 tablet daily", "stock": 90},
    {"name": "Chloroquine 250mg", "category": "General", "price": 60, "description": "Malaria ke liye", "dosage": "As directed by doctor", "stock": 120},
    {"name": "Albendazole 400mg", "category": "General", "price": 30, "description": "Worm infection ke liye", "dosage": "1 tablet single dose", "stock": 150},
    {"name": "Paracetamol Syrup", "category": "Cold & Cough", "price": 25, "description": "Bachon ke fever ke liye", "dosage": "As per weight - 10-15mg/kg", "stock": 150},
    {"name": "Calcium 500mg", "category": "Vitamins", "price": 25, "description": "Bone strength ke liye", "dosage": "1 tablet twice daily with food", "stock": 160},
    {"name": "Iron 100mg", "category": "Vitamins", "price": 20, "description": "Anemia ke liye", "dosage": "1 tablet daily on empty stomach", "stock": 150},
    {"name": "Ondansetron 4mg", "category": "Gastric", "price": 40, "description": "Nausea aur vomiting ke liye", "dosage": "1 tablet before meals", "stock": 100},
    {"name": "Loperamide 2mg", "category": "Gastric", "price": 20, "description": "Diarrhea control ke liye", "dosage": "2 tablets initially, then 1 after each loose stool", "stock": 140},
    {"name": "Levothyroxine 50mcg", "category": "General", "price": 40, "description": "Thyroid ke liye", "dosage": "1 tablet daily on empty stomach", "stock": 120},
    {"name": "Prednisolone 10mg", "category": "General", "price": 35, "description": "Inflammation ke liye", "dosage": "As directed by doctor", "stock": 130},
]

for m in medicines:
    Medicine.objects.create(**m)
    print(f"✅ Added: {m['name']}")

print(f"\n🎉 Total {Medicine.objects.count()} medicines added!")