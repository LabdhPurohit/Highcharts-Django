from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('ticket_class_view', views.ticket_class_view, name='ticket_class_view')
]