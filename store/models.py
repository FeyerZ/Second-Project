from django.db import models

# Create your models here.


class Order(models.Model):
    number = models.IntegerField(null=False)
    observation = models.CharField(max_length=50, null=True)
    numar_produse = models.IntegerField(null=True)


class Store(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    adress = models.CharField(max_length=200, null=False, default='Bucuresti')