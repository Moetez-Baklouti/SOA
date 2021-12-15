from django.urls import path
from .. import views

urlpatterns = [
    path('all/', views.get_modules),
    path('add/', views.add_module)
]
