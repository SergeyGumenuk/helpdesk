from django import forms

from tickets.models import Ticket, Answer


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
