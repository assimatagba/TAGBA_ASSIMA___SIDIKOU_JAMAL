from django.contrib import admin
from .models import Utilisateur, Depense, Budget

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Depense)
admin.site.register(Budget)
