from django import forms
from .models import patient

class patientform(forms.ModelForm):
    class Meta:
        Model=patient
        fields=[
            'name',
            'age',
            'gender',
            'phone',
            'email',
            'address',
            'blodd_group',
            'medical_history'
        ]