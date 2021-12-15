from django.db import models


class Travail_Rendre(models.Model):
    titre = models.CharField(max_length=100, null=False)
    date_lancement = models.DateTimeField(null=False)
    date_retour = models.DateTimeField(null=False)
    nature = models.CharField(max_length=50, null=False)
    descriptif = models.CharField(max_length=100, null=False)
    etudiant = models.ForeignKey('Etudiant', null=True, blank=True, on_delete=models.PROTECT)
    enseignant = models.ForeignKey('Enseignant', null=True, blank=True, on_delete=models.PROTECT)
