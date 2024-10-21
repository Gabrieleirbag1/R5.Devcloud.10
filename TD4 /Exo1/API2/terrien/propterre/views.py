from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PtForm
from . import models
from propterre.models import Pt

# Create your views here.


def index(request):
    Propterre = models.Pt.objects.all()
    return render(request, 'propterre/index.html', {'Pt_charge': Propterre})

def ajout(request):
    if request.method == "POST":
        form = PtForm(request)
        if form.is_valid(): 
            pt = form.save() 
            return render(request,"propterre/affiche.html",{"pt" : pt}) 
        else:
            return render(request,"propterre/ajout.html",{"form": form})
    else :
        form = PtForm() 
        return render(request,"propterre/ajout.html",{"form" : form})
    
    

def traitement(request):
    lform = PtForm(request.POST)
    if lform.is_valid():
        pt = lform.save()
        return HttpResponseRedirect("/propterre/")
    else:
        return render(request,"propterre/ajout.html",{"form": lform})
    
def update(request, id):
    pt = models.Pt.objects.get(pk = id)
    lform = PtForm(request.POST)
    if lform.is_valid():
        pt = lform.save(commit=False) 
        pt.id = id; 
        pt.save() 
        return HttpResponseRedirect('/propterre/')
    else:
        pt = models.Pt.objects.get(pk = id)
        lform = PtForm(instance=pt)
        return render(request, "propterre/update.html", {"form": lform, "id": id})
    

def delete(request, id):
    pt = models.Pt.objects.get(id=id)
    pt.delete()
    return HttpResponseRedirect("/propterre/")


def affiche(request, id):
    pt = models.Pt.objects.get(pk=id) 
    return render(request,"propterre/affiche.html",{"pt": pt})