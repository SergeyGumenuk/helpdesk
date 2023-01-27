from datetime import datetime

from django import forms

from appointment.models import Appointment


class AddAppointmentForm(forms.ModelForm):
    date = forms.DateField(label='', initial=datetime.today(), widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='', initial=datetime.now(),
                           widget=forms.TimeInput(attrs={'type': 'time',
                                                         'format': '%H:%M'}, format='%H:%M'))

    class Meta:
        model = Appointment
        fields = ['product', 'date', 'time']
        labels = {
            'product': '',
        }
        # widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
        #            'time': forms.TimeInput(attrs={'type': 'time'})
        #            }
