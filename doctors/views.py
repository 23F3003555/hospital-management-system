from django.shortcuts import render,redirect
from .models import Doctor
from .forms import DoctorForm
def doctor_list(request):
    doctors=Doctor.objects.all()
    
    return render(request,'doctors/doctor_list.html',
                  {'doctors':doctors}
                  )


def add_doctor(request):
    if request.method == 'POST':
        form=DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form= DoctorForm()
        return render(
         request,'doctors/add_doctor.html',
                {
                    'form': form
                }
            )



def edit_doctor(request,id):
    doctor=Doctor.objects.get(id=id)

    if request.method== 'POST':
        form=DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form=DoctorForm(instance=doctor)

    return render(
        request,
        'doctors/edit_doctor.html',{
        'form': form
        }
    )

def delete_doctor(request ,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()

    return redirect('doctor_list')