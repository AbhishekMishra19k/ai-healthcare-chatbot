from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import Doctor, Appointment

def index(request):
    specialization = request.GET.get('spec', '')
    search = request.GET.get('search', '')

    doctors = Doctor.objects.all().order_by('name')

    if specialization:
        doctors = doctors.filter(specialization=specialization)
    if search:
        doctors = doctors.filter(name__icontains=search)

    paginator = Paginator(doctors, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct().order_by('specialization')

    return render(request, 'appointments/index.html', {
        'doctors': page_obj,
        'specializations': specializations,
        'selected_spec': specialization,
        'search': search,
        'total': doctors.count(),
    })

def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_phone = request.POST['patient_phone']
        patient_email = request.POST['patient_email']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST.get('reason', '')

        appointment = Appointment.objects.create(
            patient_name=patient_name,
            patient_phone=patient_phone,
            patient_email=patient_email,
            doctor=doctor,
            date=date,
            time=time,
            reason=reason,
        )

        # User ko email
        send_mail(
            subject='Appointment Confirmed — AIHealthCare',
            message=f'''Namaste {patient_name}!

Aapka appointment confirm ho gaya hai.

Doctor: {doctor.name}
Specialization: {doctor.specialization}
Date: {date}
Time: {time}
Reason: {reason}

AIHealthCare Team''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[patient_email],
            fail_silently=True,
        )

        # Admin ko email
        send_mail(
            subject=f'New Appointment — {patient_name}',
            message=f'''Naya appointment booking hua hai!

Patient: {patient_name}
Phone: {patient_phone}
Email: {patient_email}
Doctor: {doctor.name}
Specialization: {doctor.specialization}
Date: {date}
Time: {time}
Reason: {reason}''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=True,
        )

        return redirect('appointment_success')
    return render(request, 'appointments/book.html', {'doctor': doctor})

def success(request):
    return render(request, 'appointments/success.html')