from django import forms
from .models import patient

class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields=[
            'name',
            'age',
            'gender',
            'phone',
            'email',
            'address',
            'blood_group',
            'medical_history'
        ]