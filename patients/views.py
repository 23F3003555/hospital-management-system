from django.shortcuts import render,redirect
from .models import patient
from .forms import patientform




def patient_list(request):
    patients = patient.objects.all()

    return render(
        request,
        'patients/patient_list.html',
        {
            'patients': patients
        }
    )

def add_patient(request):
    if request.method=='POST':
        form=patientform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form=patientform()
    return render(
        request,
        'patients/add_patient.html',{
            'form': form
        }
    )


def edit_patient(request,id):
    patients=patient.objects.get(id=id)

    if request.method=='POST':
        form=patientform(request.POST,instance=patients)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form=patientform(instance=patients)

        return render(
            request,
            'patients/edit_patient.html',{
                'form':form
            }
        )

def delete_patient(request,id):
    patients=patient.objects.get(id=id)
    patients.delete()
    return redirect('patients_list')