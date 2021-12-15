from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from app.models import Piece_Jointe


def get_pieces(request):
    if request.method == 'GET':
        try:
            pieces = Piece_Jointe.objects.all()
            response = json.dumps(list(map(lambda piece: {
                'id': piece.id,
                'file': piece.file.path,
                'travail': None if piece.travail_id is None else piece.travail.titre,
                'etudiant': None if piece.etudiant_id is None else piece.etudiant.nom + ' ' + piece.etudiant.prenom,
                'enseignant': None if piece.enseignant_id is None else piece.enseignant.nom + ' ' + piece.enseignant.prenom
            }, pieces)))
        except:
            response = json.dumps([{'erreur': 'Probléme dans la base de données'}])

    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_piece(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        piece = Piece_Jointe(
            id=payload['id'],
            # file=payload['file'],
            travail_id=payload['travail_id'],
            etudiant_id=payload['etudiant_id'],
            enseignant_id=payload['enseignant_id'],
        )
        try:
            piece.save()
            response = json.dumps([{'succès': 'Riece jointe a été ajouté avec succès!'}])
        except:
            response = json.dumps([{'erreur': 'Riece jointe  n\'a pas pu être ajoutée!'}])

    return HttpResponse(response, content_type='text/json')
