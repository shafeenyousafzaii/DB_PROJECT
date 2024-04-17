# DBPROJECT/urls.py
from django.urls import path
from . import views

app_name = 'DBPROJECT'
urlpatterns = [
    path('', views.index, name='index'),
]
