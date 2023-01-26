from datetime import datetime

from django import forms

from appointment.models import Appointment


class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['product', 'date', 'time']
        widgets = {'date': forms.SelectDateWidget(years=(str(datetime.now().year),)),
                   'time': forms.TimeInput(attrs={'type': 'time'})
                   }
