from django.urls import path

from products import views


app_name = 'products'


urlpatterns = [
    path('catalog/', views.get_catalog, name='catalog'),
    path('add/', views.add_product_to_catalog, name='add_product'),
    path('<slug:slug>/', views.get_product_detail, name='detail'),


]

