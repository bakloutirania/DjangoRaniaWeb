from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class user(AbstractUser):
    pass


class specialty(models.Model):
    name = models.CharField(max_length=50,unique=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    doctors = models.ManyToManyField(specialty, related_name='doctors')
    
class doctor(user):
   license_number = models.CharField(max_length=6,unique=True validators=[MinLengthValidator(6), MaxLengthValidator(6)]) 
   phone_number = models.CharField(max_length=8)
   creat_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)
   speciality=models.manyToManyField(specialty, related_name='doctors')

number_validator = RegexValidator(r'^\d{8}$', 'Phone number must be 8 digits.')


def validate_birth_date(v):
    if v> timezone.localdate():
        raise ValidationError('Birth date cannot be in the future.')

class patient(user):
    national_id = models.CharField(max_length=8,unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8,unique=True,validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



 