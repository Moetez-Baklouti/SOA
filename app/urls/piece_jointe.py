from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_pieces),
    path('add/', views.add_piece)
]
