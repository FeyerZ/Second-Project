from django.db import models

# Create your models here.
class Angajat(models.Model):
    nume = models.CharField(max_length=100, null=False)
    varsta = models.IntegerField(null=False)
    cnp = models.CharField(max_length=20, null=False)
    telefon = models.CharField(max_length=20, null=True)
    mail = models.EmailField(max_length=50, null=True, default=None)

    def __str__(self):
        return f"{self.nume} {self.cnp}"

    class Meta:
        ordering = ["-varsta", "nume"]



class Adresa(models.Model):
    strada = models.CharField(max_length=100, null=False)
    numar = models.CharField(max_length=10, null=False)
    localitate = models.CharField(max_length=100, null=False)
    judet = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True, null=False)
    angajat = models.ForeignKey(Angajat, on_delete=models.DO_NOTHING)

class Concedii(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=False)
    tip = models.CharField(max_length=2, null=False)
    angajat = models.ForeignKey(Angajat, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.angajat.nume} - start:{self.start_date} - end:{self.end_date} - tip:{self}"
class Salarii(models.Model):
    suma = models.DecimalField(decimal_places=4, max_digits=6, null=False)
    luna = models.IntegerField(null=False)
    angajat = models.ForeignKey(Angajat, on_delete=models.DO_NOTHING)