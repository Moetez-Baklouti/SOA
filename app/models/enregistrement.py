from django.db import models


class Enregistrement(models.Model):

    TYPE = [
        ('mp4', 'mp4'),
        ('flv', 'flv'),
        ('mov', 'mov'),
        ('avi', 'avi'),
        ('wmv', 'wmv')
    ]

    nom = models.CharField(max_length=100, unique=True, null=False)
    url = models.CharField(max_length=200, null=True)
    contenu = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=4, choices=TYPE)
    description = models.CharField(max_length=200, null=False)
    date = models.DateField(null=False)
    seance = models.ForeignKey('Seance', on_delete=models.PROTECT)