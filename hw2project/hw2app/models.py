from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Client #{self.pk}: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos/', null=True,
                              blank=True)

    def __str__(self):
        return f"Product #{self.pk}: {self.name}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.pk} by {self.client.name}"
