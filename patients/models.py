from django.db import models

class patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()
    blood_group=models.CharField(max_length=5)
    medical_history=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
