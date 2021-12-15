from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_enseignants),
    path('add/', views.add_enseignant)
]
