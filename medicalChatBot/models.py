from django.db import models

class Resultat(models.Model):
    plainte = models.CharField(max_length=50)
    histoire = models.CharField(max_length=50)
    examen = models.CharField(max_length=100)
    assesment = models.CharField(max_length=100)
    causes = models.CharField(max_length=100)
