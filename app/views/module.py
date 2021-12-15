from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from app.models import Module


def get_modules(request):
    if request.method == 'GET':
        try:
            modules = Module.objects.all()
            response = json.dumps(list(map(lambda module: {
                'id': module.id,
                'nom': module.nom,
                'nb_total_heure': module.nb_total_heure,
                'type': module.type,
                'niveau': Module.getNiveau(module.niveau),
                'seance': module.seance.heure_debut,
                'enseignant': module.enseignant.nom,
            }, modules)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_module(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        module = Module(
            nom=payload['nom'],
            nb_total_heure=payload['nb_total_heure'],
            type=payload['type'],
            niveau=payload['niveau'],
            seance_id=payload['seance_id'],
            enseignant_id=payload['enseignant_id'],
        )
        try:
            module.save()
            response = json.dumps([{'succès': 'Module a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Module n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
