from django.urls import path
from .views import application_form_view, success_view

urlpatterns = [
    path('', application_form_view, name='application'),
    path('success/', success_view, name='success'),
]
