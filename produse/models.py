from django.db import models

# Create your models here.
class CategoriiProduse(models.Model):
    nume=models.CharField(max_length=50, null=False)
    cantitate = models.IntegerField(null=False)
    is_active = models.BooleanField(null=False, default=True)


    def __str__(self):
        return self.nume


class Produse(models.Model):
    nume = models.CharField(max_length=50, null=False)
    pret = models.IntegerField(null=False)
    descriere = models.CharField(max_length=50, null=True)
    greutate = models.IntegerField(null=True)
    is_available = models.BooleanField(null=False, default=True)
    categorie = models.ForeignKey(CategoriiProduse, on_delete=models.CASCADE)
    # poza = models.ImageField(upload_to='media/produse', null=True)

    def __str__(self):
        return f"{self.nume} - {self.pret} - {self.descriere}"