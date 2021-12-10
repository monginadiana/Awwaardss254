from django.urls import path
from django.contrib import admin
from ratings import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('upload/project/', views.upload, name = "upload"),
    
    
    ]