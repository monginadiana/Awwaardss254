from django.urls import path
from django.contrib import admin
from ratings import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('upload/project/', views.upload_project, name = "upload"),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    
    
    ]