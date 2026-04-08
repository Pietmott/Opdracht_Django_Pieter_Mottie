from django.db import models

class BrandstofBerekening(models.Model):
    afstand = models.FloatField()
    verbruik = models.FloatField()
    prijs_per_liter = models.FloatField()
    liters = models.FloatField()
    kost = models.FloatField()

    def __str__(self):
        return f"{self.afstand} km - €{self.kost}"
