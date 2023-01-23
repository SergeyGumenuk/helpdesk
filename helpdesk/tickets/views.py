from django.shortcuts import render, get_object_or_404, redirect

from tickets.forms import CreateTicketForm
from tickets.models import Ticket


def get_not_answered_tickets(request):
    tickets = Ticket.not_answered.all()
    return render(request, 'tickets/not_answered_tickets.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/ticket/detail.html', {'ticket': ticket})


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
