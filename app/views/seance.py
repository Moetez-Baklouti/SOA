from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from app.models import Seance


def get_seances(request):
    if request.method == 'GET':
        try:
            seances = Seance.objects.all()
            response = json.dumps(list(map(lambda seance: {
                'id': seance.id,
                'heure_debut': seance.heure_debut.strftime("%H:%M"),
                'heure_fin': seance.heure_fin.strftime("%H:%M"),
                'salle': seance.salle,
                'objectif': seance.objectif,
                'resume': seance.resume,
                'etat': Seance.getEtat(seance.etat),
                'type': Seance.getType(seance.type),
                'etudiant': seance.absence.etudiant.nom + ' ' + seance.absence.etudiant.prenom
            }, seances)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_seance(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        seance = Seance(
            heure_debut=payload['heure_debut'],
            heure_fin=payload['heure_fin'],
            salle=payload['salle'],
            objectif=payload['objectif'],
            resume=payload['resume'],
            etat=payload['etat'],
            type=payload['type'],
            absence_id=payload['absence_id']
        )
        try:
            seance.save()
            response = json.dumps([{'succès': 'Séance a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Séance n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
