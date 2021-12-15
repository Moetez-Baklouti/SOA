from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('etudiant/', include('app.urls.etudiant')),
    path('groupe/', include('app.urls.groupe')),
    path('absence/', include('app.urls.absence')),
    path('seance/', include('app.urls.seance')),
    path('travail/', include('app.urls.travail_rendre')),
    path('piece/', include('app.urls.piece_jointe')),
    path('enseignant/', include('app.urls.enseignant')),
    path('module/', include('app.urls.module')),
    path('enregistrement/', include('app.urls.enregistrement'))
]
