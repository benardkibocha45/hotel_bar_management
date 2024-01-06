from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def dashboard(request):
    # Example data (replace with actual data from your models)
    revenue_graph_data = {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'values': [1000, 1500, 1200, 1800, 2000, 1900, 2200, 2300, 2100, 2400, 2600, 2700],
    }

    daily_sales_data = {
        'labels': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'values': [200, 300, 250, 400, 350, 500, 450],
    }

    sales_by_category_data = {
        'labels': ['Category A', 'Category B', 'Category C'],
        'values': [40, 35, 25],
    }

    orders_graph_data = {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'values': [50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95],
    }

    recent_activities = [
        'Added new inventory item "Item X"',
        'Updated purchase order #123',
        'Added new room #101',
        # Add more recent activities
    ]

    transactions = [
        {'date': '2023-12-31', 'amount': 500, 'description': 'Purchase from Supplier Y'},
        {'date': '2024-01-01', 'amount': 300, 'description': 'Sale of Product Z'},
        # Add more transactions
    ]

    orders = [
        {'product': 'Product A', 'total_price': 200, 'invoice_number': 'INV-001'},
        {'product': 'Product B', 'total_price': 350, 'invoice_number': 'INV-002'},
        # Add more orders
    ]

    top_selling_products = [
        {'product': 'Product C', 'quantity_sold': 100, 'price': 50},
        {'product': 'Product D', 'quantity_sold': 90, 'price': 60},
        # Add more top selling products
    ]

    most_visited_rooms = [
        {'room_number': '101', 'visits': 50},
        {'room_number': '102', 'visits': 45},
        # Add more visited rooms
    ]

    context = {
        'revenue_graph_data': revenue_graph_data,
        'daily_sales_data': daily_sales_data,
        'sales_by_category_data': sales_by_category_data,
        'orders_graph_data': orders_graph_data,
        'recent_activities': recent_activities,
        'transactions': transactions,
        'orders': orders,
        'top_selling_products': top_selling_products,
        'most_visited_rooms': most_visited_rooms,
    }
    return render(request, 'dashboard.html', context)

