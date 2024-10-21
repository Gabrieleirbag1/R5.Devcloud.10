from django.db import models

class Pt(models.Model): 

    lieu = models.CharField(max_length=100)
    surface = models.FloatField(blank=True, null = False) 
    culture = models.CharField(max_length = 100)
    renseignements = models.CharField(max_length = 100)
    date_mise = models.DateField(blank=True, null = True)
    jachere = models.BooleanField(blank=True, null = True)
    
    def __str__(self):
        chaine = f"{self.lieu} {self.surface} {self.culture} {self.renseignements}"
        return chaine





# Create your models here.
