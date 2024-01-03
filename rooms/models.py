from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    # Add other room details like type, capacity, etc.

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    # Add other booking details like dates, status, etc.
