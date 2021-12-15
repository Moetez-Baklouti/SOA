from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_etudiants),
    path('add/', views.add_etudiant),
    path('delete/<int:_id>/', views.delete_etudiant)
]
