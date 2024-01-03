from django.shortcuts import render
from .models import Item, Order

def item_list(request):
    items = Item.objects.all()
    return render(request, 'bar/item_list.html', {'items': items})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'bar/order_list.html', {'orders': orders})