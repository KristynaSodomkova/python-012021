from django.db import models

# Create your models here.
class Vypujcka(models.Model):
    datumvypujcky = models.DateField()
    datumkoncevypujcky = models.DateField()
    cenavypujcky = models.IntegerField()
    auto = models.ForeignKey("Auto", on_delete=models.SET_NULL, null=True)


class Auto(models.Model):
    registracnizn = models.CharField(max_length=20)
    znackatyp = models.CharField(max_length=100)
    najetekm = models.IntegerField()
    datkontroly = models.DateField()

    def __str__(self):
        return self.znackatyp


class Zakaznik(models.Model):
    jmenoprijm = models.CharField(max_length=100)
    ridicprukaz = models.CharField(max_length=50)
    datumnaroz = models.DateField()
    vypujcka = models.ForeignKey("Vypujcka", on_delete=models.SET_NULL, null=True)


