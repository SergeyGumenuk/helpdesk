from django.urls import path

from products import views


app_name = 'products'


urlpatterns = [
    path('catalog/', views.get_catalog, name='catalog'),
    path('add/', views.add_product_to_catalog, name='add'),
    path('delete/<int:product_id>/', views.delete_product_from_catalog, name='delete'),
    path('update/<int:product_id>/', views.update_product, name='update'),
    path('<slug:slug>/', views.get_product_detail, name='detail'),

]

