from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customers.urls', namespace='customers')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('products/', include('products.urls', namespace='products')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
