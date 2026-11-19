from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    pass


class specialty(models.Model):
    name = models.CharField(max_length=50,unique=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    doctors = models.ManyToManyField(specialty, related_name='doctors')
    
class doctor(user):
   license_number = models.CharField(max_length=6,unique=True)
   phone_number = models.CharField(max_length=8)
   creat_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)
   speciality=models.manyToManyField(specialty, related_name='doctors')

class patient(user):
    national_id = models.CharField(max_length=8,unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



