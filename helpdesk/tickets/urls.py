from django.urls import path

from tickets import views


app_name = 'tickets'


urlpatterns = [
    path('notanswered/', views.get_not_answered_tickets, name='not_answered'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('answer/<int:ticket_id>/', views.add_answer, name='add_answer'),
    path('answered/<int:ticket_id>/', views.ticket_set_answered, name='set_answered'),
    path('<int:ticket_id>/', views.ticket_detail, name='detail'),

]
