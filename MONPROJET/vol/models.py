from django.db import models

# Create your models here.
from django.db import models
class Compagnie(models.Model):
   nom = models.CharField(max_length=30)
   logo = models.CharField(max_length=30)

   def _str_(self):
        return self.nom,self.logo