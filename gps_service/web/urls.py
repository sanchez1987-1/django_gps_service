from django.urls import path
from django.views.generic import TemplateView

from .views import gps_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('map/', gps_view, name='map'),
]