from django import forms
from .models import Utilisateur, Budget, Depense

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        # On spécifie les champs qu'on souhaite afficher
        fields = ('nom', 'prenom', 'login', 'pwd')

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('budget', 'sommeEconomie', 'totalDepense')

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ('titre', 'montant')