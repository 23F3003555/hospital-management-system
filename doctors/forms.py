from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=[
            'Name',
            'Qualification',
            'Specialization',
            'Experience',
            'Phone_number',
            'Email',
            'Gender',
            'Birth_date',
            'Address',
            'consultation_Fee',
            'Department',
            'License',
            'Avalable_days',
            'joining_Date',

        ]