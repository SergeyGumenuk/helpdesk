from django.urls import path

from tickets import views


app_name = 'tickets'


urlpatterns = [
    path('notanswered/', views.get_not_answered_tickets, name='not_answered'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('<int:ticket_id>/', views.ticket_detail, name='detail'),

]
