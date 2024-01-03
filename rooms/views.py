from django.shortcuts import render
from .models import Room, Booking

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'rooms/booking_list.html', {'bookings': bookings})

def landing_page(request):
    # Add any logic or context data needed for the landing page
    return render(request, 'landing_page.html')