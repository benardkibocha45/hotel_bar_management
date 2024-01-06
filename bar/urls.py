from django.urls import path
from . import views

urlpatterns = [
# Hotel URLs
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/create/', views.hotel_create, name='hotel_create'),
    path('hotels/<int:pk>/update/', views.hotel_update, name='hotel_update'),
    path('hotels/<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),

    # Room URLs
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/create/', views.room_create, name='room_create'),
    path('rooms/<int:pk>/update/', views.room_update, name='room_update'),
    path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),

# URL patterns for PurchaseOrder views
    path('purchase_orders/', views.purchase_order_list, name='purchase_order_list'),
    path('purchase_orders/create/', views.purchase_order_create, name='purchase_order_create'),
    path('purchase_orders/<int:pk>/', views.purchase_order_detail, name='purchase_order_detail'),
    path('purchase_orders/<int:pk>/update/', views.purchase_order_update, name='purchase_order_update'),
    path('purchase_orders/<int:pk>/delete/', views.purchase_order_delete, name='purchase_order_delete'),

    # URL patterns for OrderItem views
    path('order_items/', views.order_item_list, name='order_item_list'),
    path('order_items/create/', views.order_item_create, name='order_item_create'),
    path('order_items/<int:pk>/', views.order_item_detail, name='order_item_detail'),
    path('order_items/<int:pk>/update/', views.order_item_update, name='order_item_update'),
    path('order_items/<int:pk>/delete/', views.order_item_delete, name='order_item_delete'),

    # InventoryItem URLs
    path('inventory/items/', views.inventory_item_list, name='inventory_item_list'),
    path('inventory/items/create/', views.inventory_item_create, name='inventory_item_create'),
    path('inventory/items/<int:pk>/', views.inventory_item_detail, name='inventory_item_detail'),
    path('inventory/items/<int:pk>/update/', views.inventory_item_update, name='inventory_item_update'),
    path('inventory/items/<int:pk>/delete/', views.inventory_item_delete, name='inventory_item_delete'),
    path('inventory/calculation/', views.inventory_calculation, name='inventory_calculation'),
    # Supplier URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/<int:pk>/update/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),

]

