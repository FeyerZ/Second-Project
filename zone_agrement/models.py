from django.db import models


# Create your models here.
class Orase(models.Model):
    nume = models.CharField(max_length=50, null=False)
    indicativ_judet = models.CharField(max_length=2, null=False)
    populatie = models.IntegerField(null=False)
    suprafata = models.IntegerField(null=False)


class Zone(models.Model):
    nume = models.CharField(max_length=50, null=False)
    suprafata = models.IntegerField(null=False)
    acoperit = models.BooleanField(default=False, null=False)
    oras = models.ForeignKey(Orase, on_delete=models.DO_NOTHING, null=False)


class TipuriLocatii(models.Model):
    nume = models.CharField(max_length=50, null=False)
    opening_hours = models.DateTimeField(null=False)
    closing_hours = models.DateTimeField(null=False)
    players_nr = models.IntegerField(null=False)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, null=False)
