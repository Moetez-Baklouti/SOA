from django.db import models


class Etudiant(models.Model):
    ETAT_PRESENT = 'P'
    ETAT_ABSCENT = 'A'
    ETAT_RETARD = 'R'
    ETAT_EXCLU = 'E'

    ETAT = [
        (ETAT_PRESENT, 'Présent'),
        (ETAT_ABSCENT, 'Abscent'),
        (ETAT_RETARD, 'Retard'),
        (ETAT_EXCLU, 'Exclu')
    ]

    SITUATION_NOUVEAU = 'N'
    SITUATION_REDOUBLANT = 'R'
    SITUATION_DEROGATAIRE = 'D'
    SITUATION_AUTRE = 'A'

    SITUATION = [
        (SITUATION_NOUVEAU, 'Nouveau'),
        (SITUATION_REDOUBLANT, 'Redoublant'),
        (SITUATION_DEROGATAIRE, 'Derogataire'),
        (SITUATION_AUTRE, 'Autre')
    ]

    nom = models.CharField(max_length=40, null=False)
    prenom = models.CharField(max_length=40, null=False)
    date_naissance = models.DateField(null=False)
    mail = models.CharField(max_length=70, null=False)
    photo = models.ImageField()
    etat = models.CharField(max_length=1, choices=ETAT, default=ETAT_ABSCENT)
    situation = models.CharField(max_length=1, choices=SITUATION, null=False)
    groupe = models.ForeignKey('Groupe', on_delete=models.PROTECT)

    def getEtat(char):
        etat = ''
        for e in Etudiant.ETAT:
            if e[0] == char:
                etat = e[1]

        return etat

    def getSituation(char):
        situation = ''
        for s in Etudiant.SITUATION:
            if s[0] == char:
                situation = s[1]

        return situation
