from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from django.contrib.auth.models import Group

@login_required
def dashboard(request):
    user = request.user
    if user.groups.filter(name='Doctors').exists():
        appointments = Appointment.objects.filter(doctor=user)
        role = 'Doctor'
    elif user.groups.filter(name='Nurses').exists():
        appointments = Appointment.objects.all()  # Nurses see all appointments
        role = 'Nurse'
    else:
        appointments = []
        role = 'Unknown'
    return render(request, 'dashboards/dashboard.html', {'appointments': appointments, 'role': role})
