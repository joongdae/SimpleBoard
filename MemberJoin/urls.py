from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.MemberJoinLoad ,name='MemberJoinLoad' ),
    path('Confirm1/',views.Confirm1,name='Confirm1'),
    path('Member_Insert/',views.Member_Insert,name='Member_Insert'),
]
