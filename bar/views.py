from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Room, InventoryItem, Supplier, PurchaseOrder, OrderItem
from .forms import HotelForm, RoomForm, InventoryItemForm, SupplierForm, PurchaseOrderForm, OrderItemForm
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from datetime import datetime, timedelta
# Hotel Views

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save()
            return redirect('hotel_detail', pk=hotel.pk)
    else:
        form = HotelForm()
    return render(request, 'hotel_form.html', {'form': form})

def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save()
            return redirect('hotel_detail', pk=hotel.pk)
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_form.html', {'form': form})

def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.delete()
    return redirect('hotel_list')

# Room Views (similar CRUD views for other models)

# Room Views
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_detail.html', {'room': room})

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'form': form})

def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_form.html', {'form': form})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room_confirm_delete.html', {'room': room})

# InventoryItem Views

def inventory_item_detail(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory_item_detail.html', {'inventory_item': inventory_item})

def inventory_item_list(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'inventory_item_list.html', {'inventory_items': inventory_items})

def inventory_item_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            inventory_item = form.save()
            return redirect('inventory_item_detail', pk=inventory_item.pk)
    else:
        form = InventoryItemForm()
    return render(request, 'inventory_item_form.html', {'form': form})

def inventory_item_update(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=inventory_item)
        if form.is_valid():
            inventory_item = form.save()
            return redirect('inventory_item_detail', pk=inventory_item.pk)
    else:
        form = InventoryItemForm(instance=inventory_item)
    return render(request, 'inventory_item_form.html', {'form': form})

def inventory_item_delete(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    inventory_item.delete()
    return redirect('inventory_item_list')

# Supplier Views 
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm()
    return render(request, 'supplier_form.html', {'form': form})

 
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'supplier_detail.html', {'supplier': supplier})

def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_list')

# PurchaseOrder Views
def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    return render(request, 'purchase_order_list.html', {'purchase_orders': purchase_orders})

def purchase_order_detail(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    return render(request, 'purchase_order_detail.html', {'purchase_order': purchase_order})

def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchase_order = form.save()
            return redirect('purchase_order_detail', pk=purchase_order.pk)
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchase_order_form.html', {'form': form})

def purchase_order_update(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, instance=purchase_order)
        if form.is_valid():
            purchase_order = form.save()
            return redirect('purchase_order_detail', pk=purchase_order.pk)
    else:
        form = PurchaseOrderForm(instance=purchase_order)
    return render(request, 'purchase_order_form.html', {'form': form})

def purchase_order_delete(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    purchase_order.delete()
    return redirect('purchase_order_list')

# OrderItem Views
def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'order_item_list.html', {'order_items': order_items})

def order_item_detail(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    return render(request, 'order_item_detail.html', {'order_item': order_item})


def order_item_create(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save()
            return redirect('order_item_detail', pk=order_item.pk)
    else:
        form = OrderItemForm()
    return render(request, 'order_item_form.html', {'form': form})

def order_item_update(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            order_item = form.save()
            return redirect('order_item_detail', pk=order_item.pk)
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, 'order_item_form.html', {'form': form})

def order_item_delete(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_item.delete()
    return redirect('order_item_list')



def inventory_calculation(request):
    # Calculate the total value of all inventory items
    total_inventory_value = sum(item.quantity_available * item.unit_price for item in InventoryItem.objects.all())

    # Calculate the total inventory value by category
    inventory_value_by_category = InventoryItem.objects.values('category').annotate(
        total_value=Sum(F('quantity_available') * F('unit_price'))
    )

    # Calculate the reorder suggestions
    reorder_suggestions = InventoryItem.objects.filter(quantity_available__lt=F('reorder_level'))

    # Calculate the inventory turnover ratio
    # For simplicity, assuming a fixed period and using a simple calculation
    cost_of_goods_sold = 0.6 * total_inventory_value  # Example: COGS is 60% of total inventory value

    # Calculate average inventory value
    # Assume average inventory value is the total inventory value divided by 12 months
    average_inventory_value = total_inventory_value / 12 if total_inventory_value != 0 else 0  # Example: Average inventory value over 12 months

    # Calculate inventory turnover ratio
    # Avoid division by zero by checking if average_inventory_value is not zero
    inventory_turnover_ratio = cost_of_goods_sold / average_inventory_value if average_inventory_value != 0 else 0

    # Calculate inventory ageing analysis
    # For simplicity, assuming today's date as the reference date
    today = datetime.now().date()
    inventory_ageing = {
        '1-30 days': InventoryItem.objects.filter(purchase_date__gte=today - timedelta(days=30)).count(),
        '31-60 days': InventoryItem.objects.filter(purchase_date__gte=today - timedelta(days=60),
                                                   purchase_date__lt=today - timedelta(days=30)).count(),
        # Add more age ranges as needed
    }

    # Add other calculations as per your requirements

    return render(request, 'inventory_calculation.html', {
        'total_inventory_value': total_inventory_value,
        'inventory_value_by_category': inventory_value_by_category,
        'reorder_suggestions': reorder_suggestions,
        'inventory_turnover_ratio': inventory_turnover_ratio,
        'inventory_ageing': inventory_ageing,
    })
