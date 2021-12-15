from django.db import models
from app.models import NIVEAU


class Module(models.Model):
    TYPE_OPTIONNEL = 'Op'
    TYPE_OBLIGATOIRE = 'Ob'

    TYPE = [
        (TYPE_OPTIONNEL, 'Optionnel'),
        (TYPE_OBLIGATOIRE, 'Obligatoire')
    ]

    nom = models.CharField(max_length=50, unique=True, null=False)
    nb_total_heure = models.IntegerField(null=False)
    type = models.CharField(max_length=2, choices=TYPE, null=False)
    niveau = models.CharField(max_length=2, choices=NIVEAU, null=False)
    seance = models.ForeignKey('Seance', on_delete=models.PROTECT)
    enseignant = models.ForeignKey('Enseignant', on_delete=models.PROTECT, related_name='enseignant_id')
