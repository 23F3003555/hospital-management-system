from django.shortcuts import render,redirect
from .models import Appointments
from .forms import AppointmentsForm

def appointment_list(request):
    appointments=Appointments.objects.all()

    return render(request, 'appointments/appointment_list.html',
                  {'appointments':appointments})
# Create your views here.


def add_appointments(request):
    if request.method== 'POST':
        form=AppointmentsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form=AppointmentsForm()
    return render(
        request,
        'appointments/add_appointments.html',
        {
         'form':form
        }
    )


def edit_appointments(request,id):
    appointment=Appointments.objects.get(id=id)
    if request.method== 'POST':
        form=AppointmentsForm(request.POST,instance=appointment)
        if form.is_valid():
         form.save()
         return redirect('appointment_list')
    else:
        form=AppointmentsForm(instance=appointment)
    return render(
        request,
        'appointments/edit_appointment.html',
        {
            'form':form
        }
    )


def delete_appointment(request,id):
    appointment=Appointments.objects.get(id=id)
    appointment.delete()

    return redirect('appointment_list')