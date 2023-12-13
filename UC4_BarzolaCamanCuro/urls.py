from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto/', include('proyecto.urls')),
    path('', include('proyecto.urls')),
]