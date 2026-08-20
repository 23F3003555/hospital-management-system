from django.db import models

from patients.models import patient
from doctors.models import Doctor

class Appointments(models.Model):
    Patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor,on_delete= models.CASCADE)
    Appointments_date=models.DateField()
    Appointments_time=models.TimeField()
    Reason=models.CharField(max_length=200)
    Status=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Patient} - {self.Doctor}"

# Create your models here.
