from django.urls import path

from customers import views


app_name = 'customers'


urlpatterns = [
    path('', views.index, name='home'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout'),
    path('user/register/', views.user_register, name='registration'),
    path('user/profile/edit/', views.profile_edit, name='profile_edit'),
    path('user/profile/delete/', views.profile_delete, name='profile_delete'),
    path('user/profile/<str:username>/', views.profile_detail, name='profile_detail'),

]
