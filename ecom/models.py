from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=100, null=False)

class Orders(models.Model):
    order_date = models.DateField(null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Shippments(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)
