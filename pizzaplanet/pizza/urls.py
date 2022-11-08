from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cheese/', views.cheese),
    path('pepperoni/', views.pepperoni),
]