from django.urls import path

from appointment import views


app_name = 'appointment'


urlpatterns = [
    path('add/', views.add_appointment, name='add'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete'),
]
