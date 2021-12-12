from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('login/dena/' , views.dena),
    path('login/lena/' , views.lena),
    
]