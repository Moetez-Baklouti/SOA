from django.db import models
from app.models import NIVEAU


class Groupe(models.Model):
    nom = models.CharField(max_length=8, null=False)
    nb_etudiants = models.IntegerField(null=False)
    mail = models.CharField(max_length=70, null=False)
    niveau = models.CharField(max_length=2, choices=NIVEAU)
