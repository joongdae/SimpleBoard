from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.writeboard1, name="SelectBoard"),
    path('Board_Insert/', views.Board_Insert, name="Board_Insert"),
]
