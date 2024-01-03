from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    # Add other item details like price, quantity, etc.

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # Add other order details like date, status, etc.
