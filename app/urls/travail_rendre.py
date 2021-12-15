from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_travaux),
    path('add/', views.add_travail)
]
