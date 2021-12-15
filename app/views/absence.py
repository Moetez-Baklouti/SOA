from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from app.models import Absence


def get_absences(request):
    if request.method == 'GET':
        try:
            absences = Absence.objects.all()
            response = json.dumps(list(map(lambda absence: {
                'id': absence.id,
                'date': absence.date.strftime('%d/%m/%Y'),
                'motif': absence.motif,
                'justificatif': absence.justificatif,
                'etudiant': absence.etudiant.nom + ' ' + absence.etudiant.prenom,
                'groupe': absence.etudiant.groupe.nom
            }, absences)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_absence(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        absence = Absence(
            date=datetime.strptime(payload['date'], '%d/%m/%Y'),
            motif=payload['motif'],
            justificatif=payload['justificatif'],
            etudiant_id=payload['etudiant_id']
        )
        try:
            absence.save()
            response = json.dumps([{'succès': 'Absence a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Absence n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
