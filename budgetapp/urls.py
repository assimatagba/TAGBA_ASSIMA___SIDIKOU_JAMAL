from django.contrib import admin
from django.urls import path
from . import views

app_name="budgetapp"

urlpatterns = [
    path('liste_depense', views.liste_depense, name='liste_depense'),
    path('historique_depense', views.historique_depense, name='historique_depense'),
    path('login/',views.login,name='login'),
    path('espace_utilisateur', views.espace_utilisateur, name='espace_utilisateur'),
    path('budgetapp/liste_depense', views.liste_depense, name='budgetapp/liste_depense'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('ajouter_depense', views.ajouter_depense, name='ajouter_depense'),
    path('supprimer_depense:<int:id>', views.supprimer_depense, name='supprimer_depense'),
    path('ajouter_budget', views.ajouter_budget, name='ajouter_budget'),
    path('modifier_depense:<int:id>', views.modifier_depense, name="modifier_depense"),
    path('modifier_utilisateur', views.modifier_utilisateur, name="modifier_utilisateur")
]
