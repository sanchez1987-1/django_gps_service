from django.urls import path
from django.views.generic import TemplateView

from .views import gps_view

from django.contrib import admin, auth
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('map/', gps_view, name='map'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]