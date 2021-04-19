from django.db import models

# Create your models here.
class Auto(models.Model):
    registracnizn = models.CharField(max_length=20)
    znackatyp = models.CharField(max_length=100)
    najetekm = models.IntegerField()
    datkontroly = models.DateField()

class Zakaznik(models.Model):
    jmenoprijm = models.CharField(max_length=100)
    ridicprukaz = models.CharField(max_length=50)
    datumnaroz = models.DateField()

class Vypujcka(models.Model):
    datumvypujcky = models.DateField()
    datumkoncevypujcky = models.DateField()
    cenavypujcky = models.IntegerField()
