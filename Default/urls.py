from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.DefaultLoad ,name='DefaultLoad' ),
    path('MemberJoin/', include('MemberJoin.urls'),name='MemberJoin'),
    path('LoginClick/', views.LoginClick,name='LoginClick'),
    path('List/', include('BoardList.urls'),name='BoardList'),
]
