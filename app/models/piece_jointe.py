from django.db import models


class Piece_Jointe(models.Model):
    nom = models.CharField(max_length=200, null=False)
    file = models.FileField(upload_to='uploads')
    travail = models.ForeignKey('Travail_Rendre', null=True, blank=True, on_delete=models.PROTECT)
    etudiant = models.ForeignKey('Etudiant', null=True, blank=True, on_delete=models.PROTECT)
    enseignant = models.ForeignKey('Enseignant', null=True, blank=True, on_delete=models.PROTECT)
