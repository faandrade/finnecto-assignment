from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)


class Order(models.Model):
    STATUS_CHOICES = [
        ("APPROVED", "Approved"),
        ("APPROVING", "Approving"),
        ("REJECTED", "Rejected"),
    ]
    TYPE_CHOICES = [
        ("NEGOTIATED", "Negotiated"),
        ("NOT_CATALOGUED", "Not Catalogued"),
        ("NOT_CATALOGUED", "Not Catalogued"),
    ]

    requester = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders"
    )
    description = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    date = models.DateTimeField()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders"
    )
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    currency = models.CharField(max_length=3)
