from django.shortcuts import render
from .models import Patient, MedicalHistory
from django.contrib.auth.decorators import login_required

@login_required
def patient_history(request):
    patient = Patient.objects.get(user=request.user)
    history = MedicalHistory.objects.filter(patient=patient)
    return render(request, 'patients/history.html', {'patient': patient, 'history': history})