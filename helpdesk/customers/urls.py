from django.urls import path

from customers import views


app_name = 'customers'


urlpatterns = [
    path('', views.index, name='home'),
    path('user/login/', views.user_login, name='login'),
]
