"""
URL configuration for dextApi project.

"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import homepage

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage),
    path('api/', include('accounts.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
