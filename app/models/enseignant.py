from django.db import models


class Enseignant(models.Model):
    nom = models.CharField(max_length=40, null=False)
    prenom = models.CharField(max_length=40, null=False)
    mail_personnelle = models.CharField(max_length=70, null=False)
    mail_travail = models.CharField(max_length=70, null=False)
    nb_heure = models.IntegerField(null=False)
    photo = models.ImageField()
    module = models.ForeignKey('Module', on_delete=models.PROTECT, related_name='module_id')
