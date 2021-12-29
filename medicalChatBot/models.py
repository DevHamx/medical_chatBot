from django.db import models

class Resultat(models.Model):
    plainte = models.CharField(max_length=50)
    description = models.CharField(max_length=9999)
    probability = models.CharField(max_length=10)
    precaution = models.CharField(max_length=100)