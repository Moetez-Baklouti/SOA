from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_absences),
    path('add/', views.add_absence)
]
