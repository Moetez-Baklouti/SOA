NIVEAU_L1 = 'L1'
NIVEAU_L2 = 'L2'
NIVEAU_L3 = 'L3'
NIVEAU_M1 = 'M1'
NIVEAU_M2 = 'M2'

NIVEAU = [
    (NIVEAU_L1, '1 er License'),
    (NIVEAU_L2, '2 éme License'),
    (NIVEAU_L3, '3 éme License'),
    (NIVEAU_M1, '1 er Mastére'),
    (NIVEAU_M2, '2 éme Mastére')
]


def getNiveau(char):
    niveau = ''
    for s in NIVEAU:
        if s[0] == char:
            niveau = s[1]

    return niveau


from .absence import Absence
from .enregistrement import Enregistrement
from .enseignant import Enseignant
from .etudiant import Etudiant
from .groupe import Groupe
from .module import Module
from .piece_jointe import Piece_Jointe
from .seance import Seance
from .travail_rendre import Travail_Rendre
