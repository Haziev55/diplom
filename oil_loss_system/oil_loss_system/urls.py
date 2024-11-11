from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oil_loss.urls')),
    path('', include('oil_loss.api_urls')),
]
