from django.urls import path

from app import views


urlpatterns = [
    path('all/', views.get_enregistrements),
    path('add/', views.add_enregistrement)
]
