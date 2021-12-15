from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import json

from app.models import Travail_Rendre


def get_travaux(request):
    if request.method == 'GET':
        try:
            travaux = Travail_Rendre.objects.all()
            response = json.dumps(list(map(lambda travail: {
                'id': travail.id,
                'titre': travail.titre,
                'date_lancement': travail.date_lancementstrftime('%d/%m/%Y'),
                'date_retour': travail.date_retourstrftime('%d/%m/%Y'),
                'nature': travail.nature,
                'descriptif': travail.descriptif,
                'etudiant': travail.etudiant.nom + ' ' + travail.etudiant.prenom,
                'enseignant': travail.enseignant.nom + ' ' + travail.enseignant.prenom
            }, travaux)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_travail(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        travail = Travail_Rendre(
            titre=payload['titre'],
            date_lancement=datetime.strptime(payload['date_lancement'], '%d/%m/%Y'),
            date_retour=datetime.strptime(payload['date_retour'], '%d/%m/%Y'),
            nature=payload['nature'],
            descriptif=payload['descriptif'],
            etudiant_id=payload['etudiant_id'],
            enseignant_id=payload['enseignant_id']
        )
        try:
            travail.save()
            response = json.dumps([{'succès': 'Travail a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Travail n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
