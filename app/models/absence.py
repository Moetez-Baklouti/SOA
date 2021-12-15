from django.db import models


class Absence(models.Model):
    date = models.DateField(null=False)
    motif = models.TextField(max_length=200, null=True)
    justificatif = models.TextField(max_length=200, null=True)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
