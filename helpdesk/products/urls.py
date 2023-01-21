from django.urls import path

from products import views


app_name = 'products'


urlpatterns = [
    path('catalog/', views.get_catalog, name='catalog'),
    path('<slug:slug>/', views.get_product_detail, name='detail'),

]

