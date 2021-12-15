from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import json

from app.models import Enregistrement


def get_enregistrements(request):
    if request.method == 'GET':
        try:
            enregistrements = Enregistrement.objects.all()
            response = json.dumps(list(map(lambda enregistrement: {
                'id': enregistrement.id,
                'nom': enregistrement.nom,
                'url': enregistrement.url,
                'contenu': enregistrement.contenu,
                'type': enregistrement.type,
                'description': enregistrement.description,
                'date': enregistrement.date,
                'seance': enregistrement.seance.heure_debut ,
            }, enregistrements)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_enregistrement(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        enregistrement = Enregistrement(
            nom=payload['nom'],
            url=payload['url'],
            contenu=payload['contenu'],
            type=payload['type'],
            description=payload['description'],
            date=datetime.strptime(payload['date_naissance'], '%d/%m/%Y'),
            seance_id=payload['seance_id']
        ) 
        try:
            enregistrement.save()
            response = json.dumps([{'succès': 'Enregistrement a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Enregistrement n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
