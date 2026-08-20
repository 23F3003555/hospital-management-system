from django.db import models

class Doctor(models.Model):
    Name=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=15)
    Specialization=models.CharField(max_length=50)
    Experience=models.IntegerField()
    Phone_number=models.CharField(max_length=15)
    Email=models.EmailField()
    Gender=models.CharField(max_length=10)
    Birth_date=models.DateField()
    Address=models.CharField(max_length=100)
    consultation_Fee=models.CharField(max_length=10)
    Department=models.CharField(max_length=20)
    License=models.CharField(max_length=50)
    Avalable_days=models.CharField(max_length=100)
    joining_Date=models.DateField()



    def __str__(self):
        return self.Name

# Create your models here.
