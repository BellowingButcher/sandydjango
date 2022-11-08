from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cheese/', views.index, name='cheese'),
    path('pepperoni/', views.index, name='pepperoni'),
]