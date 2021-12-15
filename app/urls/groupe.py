from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_groupes),
    path('add/', views.add_groupe)
]
