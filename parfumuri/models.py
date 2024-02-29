from django.db import models

# Create your models here.
class Parfumuri(models.Model):
    nume = models.CharField(max_length=100, null=False)
    greutate = models.DecimalField(decimal_places=4, max_digits=6)
    culoare = models.CharField(max_length=20, null=True)
    descriere = models.CharField(max_length=100, null=True)

class Producatori(models.Model):
    nume = models.CharField(max_length=100, null=False)
    tara = models.CharField(max_length=100, null=True)
    cui = models.IntegerField(null=False)
    parfum = models.ForeignKey(Parfumuri, on_delete=models.DO_NOTHING)

class Ingrediente(models.Model):
    nume = models.CharField(max_length=100, null=False)
    gramaj = models.DecimalField(decimal_places=4, max_digits=6)
    cost = models.DecimalField(decimal_places=4, max_digits=6)
    parfum = models.ManyToManyField(Parfumuri)
