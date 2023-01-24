from django.contrib import admin

from tickets.models import Ticket, Answer


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['pk', 'created', 'answered']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'ticket', 'created']
