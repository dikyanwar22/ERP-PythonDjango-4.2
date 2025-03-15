from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('erp.urls')),  # untuk ERP
    path('api/', include('api.urls')),  # untuk API
]
