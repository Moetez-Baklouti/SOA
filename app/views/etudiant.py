from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import json

from app.models import Etudiant


def get_etudiants(request):
    if request.method == 'GET':
        try:
            etudiants = Etudiant.objects.all()
            response = json.dumps(list(map(lambda etudiant: {
                'id': etudiant.id,
                'nom': etudiant.nom,
                'prenom': etudiant.prenom,
                'date_naissance': etudiant.date_naissance.strftime('%d/%m/%Y'),
                'mail': etudiant.mail,
                'etat': Etudiant.getEtat(etudiant.etat),
                'situation': Etudiant.getSituation(etudiant.situation),
                'group': etudiant.groupe.nom
            }, etudiants)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_etudiant(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        etudiant = Etudiant(
            nom=payload['nom'],
            prenom=payload['prenom'],
            date_naissance=datetime.strptime(payload['date_naissance'], '%d/%m/%Y'),
            mail=payload['mail'],
            etat=payload['etat'],
            situation=payload['situation'],
            groupe_id=payload['groupe_id']
        )
        try:
            etudiant.save()
            response = json.dumps([{'succès': 'Etudiant a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Etudiant n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')


def delete_etudiant(request, _id):
    if request.method == 'GET':
        try:
            etudiant = Etudiant.objects.get(pk=_id)
            etudiant.delete()
            response = json.dumps([{'succès': 'Etudiant a été supprimé avec succès!'}])
        except:
            response = json.dumps([{'error': 'Acune étudiant dont l\'id = ' + str(_id)}])
    return HttpResponse(response, content_type='text/json')