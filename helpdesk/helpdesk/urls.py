from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customers.urls', namespace='customers')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('products/', include('products.urls', namespace='products')),

]
