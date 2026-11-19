from django.db import models
from accountApp.models import doctor, patient
# Create your models here.
class Appointment(models.Model):
    reason = models.CharField()
    prescription = models.CharField(
    blank = True,
    upload_to = 'prescriptions/',
    )
class  status(models.Textfield):
    PENDING = 'Pending' "en attente"
    CONFIRMED = 'Confirmed' , "confirmé"
    CANCELED = 'Canceled' , "annulé"
    status=models.CharField(max_length=10, choices=status.choices, default=status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(patient, on_delete=models.CASCADE, related_name='appointments') 
    