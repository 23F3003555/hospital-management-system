from django import forms

from .models import Appointments

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model=Appointments
        fields='__all__'