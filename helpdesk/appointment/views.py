from django.shortcuts import render, redirect

from appointment.forms import AddAppointmentForm
from appointment.models import Appointment


def add_appointment(request):
    if request.method == 'POST':
        form = AddAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('customers:profile_detail', request.user.username)
    else:
        form = AddAppointmentForm()

    return render(request, 'appointment/add.html', {'form': form})


def delete_appointment(request, appointment_id):
    Appointment.objects.filter(pk=appointment_id).delete()
    return redirect('customers:profile_detail', request.user.username)
