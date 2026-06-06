from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import Doctor, Appointment


def index(request):
    specialization = request.GET.get('spec', '')
    search         = request.GET.get('search', '')

    doctors = Doctor.objects.all().order_by('name')
    if specialization:
        doctors = doctors.filter(specialization=specialization)
    if search:
        doctors = doctors.filter(name__icontains=search)

    paginator = Paginator(doctors, 12)
    page_obj  = paginator.get_page(request.GET.get('page', 1))

    specializations = Doctor.objects.values_list(
        'specialization', flat=True
    ).distinct().order_by('specialization')

    return render(request, 'appointments/index.html', {
        'doctors':        page_obj,
        'specializations': specializations,
        'selected_spec':  specialization,
        'search':         search,
        'total':          doctors.count(),
    })


def book_appointment(request, doctor_id):
    # 404 instead of 500 if doctor not found
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        patient_name  = request.POST.get('patient_name', '').strip()
        patient_phone = request.POST.get('patient_phone', '').strip()
        patient_email = request.POST.get('patient_email', '').strip()
        date          = request.POST.get('date', '')
        time          = request.POST.get('time', '')
        reason        = request.POST.get('reason', '')

        if not all([patient_name, patient_phone, patient_email, date, time]):
            return render(request, 'appointments/book.html', {
                'doctor': doctor,
                'error': 'Sab fields fill karo.',
            })

        Appointment.objects.create(
            patient_name=patient_name,
            patient_phone=patient_phone,
            patient_email=patient_email,
            doctor=doctor,
            date=date,
            time=time,
            reason=reason,
        )

        # Email — only if email backend is configured
        from_email  = (getattr(settings, 'DEFAULT_FROM_EMAIL', '') or '').strip()
        admin_email = (getattr(settings, 'ADMIN_EMAIL', '') or '').strip()

        if patient_email and from_email:
            try:
                send_mail(
                    subject='Appointment Confirmed — AIHealthCare',
                    message=(
                        f"Namaste {patient_name}!\n\n"
                        f"Aapka appointment confirm ho gaya hai.\n\n"
                        f"Doctor        : {doctor.name}\n"
                        f"Specialization: {doctor.specialization}\n"
                        f"Date          : {date}\n"
                        f"Time          : {time}\n"
                        f"Reason        : {reason}\n\n"
                        f"AIHealthCare Team\n"
                        f"Emergency: 108 | Ambulance: 102"
                    ),
                    from_email=from_email,
                    recipient_list=[patient_email],
                    fail_silently=True,
                )
            except Exception as e:
                if settings.DEBUG:
                    print(f"[Email Error] {e}")

        if admin_email and from_email:
            try:
                send_mail(
                    subject=f'New Appointment — {patient_name}',
                    message=(
                        f"Naya appointment!\n\n"
                        f"Patient : {patient_name}\n"
                        f"Phone   : {patient_phone}\n"
                        f"Doctor  : {doctor.name} ({doctor.specialization})\n"
                        f"Date    : {date}  Time: {time}\n"
                        f"Reason  : {reason}"
                    ),
                    from_email=from_email,
                    recipient_list=[admin_email],
                    fail_silently=True,
                )
            except Exception as e:
                if settings.DEBUG:
                    print(f"[Email Error] {e}")

        return redirect('appointment_success')

    return render(request, 'appointments/book.html', {'doctor': doctor})


def success(request):
    return render(request, 'appointments/success.html')