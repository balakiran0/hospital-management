from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Doctors'})
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.date}"