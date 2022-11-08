from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.get_all_pizzas),
    path('orders/<str:name>/', views.get_orders_by_person),
    path('orders/<int:id>/', views.all_orders_by_id),
]