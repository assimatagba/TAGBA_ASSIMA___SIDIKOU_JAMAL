from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    login = models.CharField(max_length=60)
    pwd = models.CharField(max_length=60)

class Budget(models.Model):
    budget = models.FloatField(default=0)
    totalDepense = models.FloatField(default=0)
    sommeEconomie = models.FloatField(default=0)
    budgetRestant = models.FloatField(default=0)
    user = models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True,blank=True)


class Depense(models.Model):
    titre = models.CharField(max_length=100)
    montant = models.IntegerField()
    date_depense = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True,blank=True)
