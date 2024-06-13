from django.contrib import admin
from django.urls import path
from . import views

rlpatterns = [
    path('', views.index, name='index'),
]