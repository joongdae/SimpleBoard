from django.contrib import admin
from django.urls import path,include
from . import views

app_name='BoardList'
urlpatterns = [
    path('', views.BoardListLoad ,name='BoardListLoad' ),
    path('viewdata/<int:id>/', views.viewdata1, name="viewdata"),
    path('Itemdelete/<int:id>/', views.Itemdelete, name="Itemdelete"),
    path('ItemSave/', views.ItemSave, name="ItemSave"),
    path('writeboard/', include('WriteBoard.urls'), name="WriteBoard"),
    path('logout', views.logout, name="logout"),
]
