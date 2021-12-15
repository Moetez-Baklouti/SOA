from django.db import models


class Seance(models.Model):
    ETAT_ENCOURS = 'E'
    ETAT_TERMINEE = 'T'
    ETAT_ANNULEE = 'A'
    ETAT_DIFFEREE = 'D'

    ETAT = [
        (ETAT_ENCOURS, 'En cours'),
        (ETAT_TERMINEE, 'Terminée'),
        (ETAT_ANNULEE, 'Annulée'),
        (ETAT_DIFFEREE, 'Différée')
    ]

    TYPE_NORMALE = 'N'
    TYPE_RATRAPAGE = 'R'
    TYPE_SOUTIEN = 'S'
    TYPE_FORMATION = 'F'

    TYPE = [
        (TYPE_NORMALE, 'Normale'),
        (TYPE_RATRAPAGE, 'Ratrapage'),
        (TYPE_SOUTIEN, 'Soutien'),
        (TYPE_FORMATION, 'Formation')
    ]

    heure_debut = models.TimeField(null=False)
    heure_fin = models.TimeField(null=False)
    salle = models.CharField(max_length=10, default='En ligne')
    objectif = models.CharField(max_length=50, null=False)
    resume = models.CharField(max_length=100, null=False)
    etat = models.CharField(max_length=1, choices=ETAT)
    type = models.CharField(max_length=1, choices=TYPE)
    absence = models.OneToOneField('Absence', on_delete=models.CASCADE)

    def getEtat(char):
        etat = ''
        for e in Seance.ETAT:
            if e[0] == char:
                etat = e[1]

        return etat

    def getType(char):
        type = ''
        for t in Seance.TYPE:
            if t[0] == char:
                type = t[1]

        return type
