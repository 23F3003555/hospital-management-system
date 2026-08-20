from django.shortcuts import render

from patients.models import patient
from doctors.models import Doctor
from appointments.models import Appointments


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    doctor_count = Doctor.objects.count()
    patient_count = patient.objects.count()
    appointment_count = Appointments.objects.count()

    recent_appointments = Appointments.objects.all().order_by('-Appointments_date')[:2]

    active_count=Appointments.objects.filter(Status='Active').count()
    pending_count=Appointments.objects.filter(Status='Pending').count()
    completed_count=Appointments.objects.filter(Status='Complete').count()

    return render(
        request,
        'home/dashboard.html',
        {
            'doctor_count': doctor_count,
            'patient_count': patient_count,
            'appointment_count': appointment_count,
            'recent_appointments': recent_appointments,
            'active_count':active_count,
            'pending_count':pending_count,
            'completed_count':completed_count
        }
    )