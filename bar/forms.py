from django import forms
from .models import Hotel, Room, InventoryItem, Supplier, PurchaseOrder, OrderItem

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'contact_info', 'star_rating', 'amenities', 'description']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'room_type', 'rate', 'availability', 'description', 'image']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'category', 'quantity_available', 'unit_price', 'reorder_level', 'expiry_date', 'location', 'supplier_info']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'address', 'email', 'phone_number']

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'order_date', 'delivery_date', 'status', 'total_amount', 'shipping_address', 'payment_status']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'item', 'quantity', 'unit_price']
