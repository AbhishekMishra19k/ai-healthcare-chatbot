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

        # Email sending (guard against missing configuration to avoid 500 errors)
        default_from_email = (getattr(settings, 'DEFAULT_FROM_EMAIL', '') or '').strip()
        admin_email = (getattr(settings, 'ADMIN_EMAIL', '') or '').strip()
        patient_email = (patient_email or '').strip()

        # User ko email
        if patient_email and default_from_email:
            try:
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
                    from_email=default_from_email,
                    recipient_list=[patient_email],
                    fail_silently=True,
                )
            except TypeError:
                pass

        # Admin ko email
        if admin_email and default_from_email:
            try:
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
                    from_email=default_from_email,
                    recipient_list=[admin_email],
                    fail_silently=True,
                )
            except TypeError:
                pass



        return redirect('appointment_success')
    return render(request, 'appointments/book.html', {'doctor': doctor})



def success(request):

    return render(request, 'appointments/success.html')