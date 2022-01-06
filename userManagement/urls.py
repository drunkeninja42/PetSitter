from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('route/', views.route),
    path('map/', views.map),
    path('login/', views.login),
    path('signup/', views.signup),
]