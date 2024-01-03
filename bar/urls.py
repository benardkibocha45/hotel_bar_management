from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('orders/', views.order_list, name='order_list'),
    # Add other URLs as needed
]
