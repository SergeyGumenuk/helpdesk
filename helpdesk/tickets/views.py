from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from tickets.forms import CreateTicketForm, AddAnswerForm
from tickets.models import Ticket, Answer


def get_not_answered_tickets(request):
    tickets = Ticket.not_answered.all()
    return render(request, 'tickets/not_answered_tickets.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    answer_form = AddAnswerForm()
    answers = ticket.answers.all()
    return render(request, 'tickets/ticket/detail.html', {'ticket': ticket,
                                                          'answer_form': answer_form,
                                                          'answers': answers})


def ticket_create(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('tickets:detail', ticket.id)
    else:
        form = CreateTicketForm()

    return render(request, 'tickets/ticket/create.html', {'form': form})


@require_POST
def ticket_set_answered(request, ticket_id):
    Ticket.not_answered.filter(pk=ticket_id).update(answered=True)
    return redirect('tickets:not_answered')


@require_POST
def add_answer(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    Answer.objects.create(user=request.user,
                          ticket=ticket,
                          content=request.POST['content'])
    return redirect('tickets:detail', ticket_id)
