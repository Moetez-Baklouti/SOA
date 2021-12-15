from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from app.models import Groupe
from app.models import getNiveau

def get_groupes(request):
    if request.method == 'GET':
        try:
            groupes = Groupe.objects.all()
            response = json.dumps(list(map(lambda groupe: {
                'id': groupe.id,
                'nom': groupe.nom,
                'nb_etudiants': groupe.nb_etudiants,
                'mail': groupe.mail,
                'niveau': getNiveau(groupe.niveau)
            }, groupes)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_groupe(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        groupe = Groupe(
            nom=payload['nom'],
            nb_etudiants=payload['nb_etudiants'],
            mail=payload['mail'],
            niveau=payload['niveau']
        )
        try:
            groupe.save()
            response = json.dumps([{'succès': 'Groupe a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Groupe n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
