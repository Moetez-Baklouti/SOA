from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import json

from app.models import  Enseignant


def get_enseignants(request):
    if request.method == 'GET':
        try:
            enseignants = Enseignant.objects.all()
            response = json.dumps(list(map(lambda enseignant: {
                'id': enseignant.id,
                'nom': enseignant.nom,
                'prenom': enseignant.prenom,
                'mail_personnelle': enseignant.mail_personnelle,
                'mail_travail': enseignant.mail_travail,
                'nb_heure': enseignant.nb_heure,
                'photo': enseignant.photo,
                'module': enseignant.module.nom ,
            }, enseignants)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_enseignant(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        enseignant = Enseignant(
            nom=payload['nom'],
            prenom=payload['prenom'],
            mail_personnelle=payload['mail_personnelle'],
            mail_travail=payload['mail_travail'],
            nb_heure=payload['nb_heure'],
            photo=datetime.strptime(payload['date_naissance'], '%d/%m/%Y'),
            module_id=payload['module_id']
        ) 
        try:
            enseignant.save()
            response = json.dumps([{'succès': 'enseignant a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'enseignant n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')