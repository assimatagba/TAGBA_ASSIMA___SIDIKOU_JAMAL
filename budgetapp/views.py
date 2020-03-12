from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib import messages
import time

from .models import Depense
from .models import Utilisateur
from .models import Budget
from datetime import datetime

from .forms import UtilisateurForm, BudgetForm, DepenseForm


# Create your views here.
def home (request):
    return render(request,'budgetapp/home.html')

def liste_depense(request):
    if not ('pk' in request.session):
        return redirect('budgetapp:login')
    else:
        utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
        now_date = datetime.now()
        now_month = now_date.month
        listes_depenses = Depense.objects.filter(user=utilisateur, date_depense__month=now_month)
    return render(request, 'budgetapp/dashboard/liste_depense.html', {'listes_depenses': listes_depenses, 'utilisateur': utilisateur, 'now_date':now_date})

def historique_depense(request):
    utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
    budgets = Budget.objects.filter(user=utilisateur)
    listes_depenses = Depense.objects.filter(user=utilisateur)
    return render(request, 'budgetapp/dashboard/historique_depense.html', {'listes_depenses': listes_depenses, 'utilisateur': utilisateur, 'budgets': budgets})

def init_budget():
    depenses = Depense.objects.all()
    for depense in depenses:
        depense.budgetRestant = depense.budget - depense.totalDepense
        depense.save()


def registration(request):
    if request.method == "POST":
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            request.session['pk'] = form.save().pk
            return redirect('budgetapp:ajouter_budget')
    else:
        form = UtilisateurForm()
    return render(request,'budgetapp/inscription.html', {'form' : form})

def ajouter_budget(request):
    if not ('pk' in request.session):
        return redirect('budgetapp:login')
    else:
        if request.method == "POST":
            form = BudgetForm(request.POST)
            if form.is_valid():
                depense = form.save(commit=False)
                depense.budgetRestant = depense.budget - depense.totalDepense
                utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
                depense.user = utilisateur
                depense.save()
                return redirect('budgetapp:espace_utilisateur')
        else:
            form = BudgetForm()
    return render (request, 'budgetapp/dashboard/ajouter_budget.html')

def login(request):
    if request.method == "POST":
        users = Utilisateur.objects.filter(login=request.POST['login'])
        for user in users:
            if(user.login == request.POST['login'] and user.pwd == request.POST['pwd']):
                request.session['pk'] = user.pk
                return redirect('budgetapp:espace_utilisateur')        
    return render(request,'registration/login.html')

def logout(request):
    try:
        del request.session['pk']
    except KeyError:
        pass
    return redirect('budgetapp:home')

def espace_utilisateur(request):
    utilisateur = Utilisateur.objects.get(pk=request.session['pk'])

    return render(request,'budgetapp/dashboard/espace_utilisateur.html', {'utilisateur': utilisateur})

def ajouter_depense(request):
    if not ('pk' in request.session):
        return redirect('budgetapp:login')
    else:
        utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
        info_depense = Budget.objects.get(user=utilisateur)
        if request.method == "POST":
            form = DepenseForm(request.POST)
            if form.is_valid():
                depense = form.save(commit=False)
                depense.user = utilisateur
                if(info_depense.budgetRestant >= depense.montant):
                    info_depense.budgetRestant -= depense.montant
                    depense.save()
                    info_depense.save()
                    return redirect('budgetapp:liste_depense')
        else:
            form = DepenseForm()
    return render(request,'budgetapp/dashboard/ajouter_depense.html', {'form' : form, 'utilisateur': utilisateur})

def modifier_depense(request,id):
    depense = Depense.objects.get(pk=id) 
    utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
    info_depense = Budget.objects.get(user=utilisateur)
    info_depense.budgetRestant += depense.montant
    if request.method == "POST":
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            depense = form.save(commit=False)
            depense.user = utilisateur
            if(info_depense.budgetRestant >= depense.montant):
                    info_depense.budgetRestant -= depense.montant
                    depense.save()
                    info_depense.save()
                    return redirect('budgetapp:liste_depense')
            else:
                messages.error(request,"Votre budget restant ne vous permet pas d'ajouter cette depense")
        
    form = DepenseForm(instance=depense)
    return render(request, 'budgetapp/dashboard/modifier_depense.html', {'form':form, 'utilisateur': utilisateur})

def supprimer_depense(request,id):
    del_depense = Depense.objects.get(pk=id)
    del_depense.delete()

    return redirect('budgetapp:liste_depense')
def modifier_utilisateur(request):
    utilisateur = Utilisateur.objects.get(pk=request.session['pk'])
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('budgetapp:espace_utilisateur')
        
    form = UtilisateurForm(instance=utilisateur)
    return render(request, 'budgetapp/dashboard/modifier_utilisateur.html', {'form': form, 'utilisateur': utilisateur})

def notifier():
    notification = win10toast.ToastNotifier()
    notification.show_toast(" N'oubliez pas de renseigner vos depenses effectué ! ")