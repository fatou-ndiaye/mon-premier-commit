from django.shortcuts import render
from django.http import HttpResponse
from .models import Vol,Compagnie

# Create your views here.

def home(request):
    #a="BIENVENUE DANS HOME"
    vol=Vol.objects.all()
    compagnie=Compagnie.objects.all()
    
    
    
    #a="bonjour"
    #vol=Vol

    #return HttpResponse(vol)
    return render(request,'home.html',locals())

def listcomp(request,vol_d):
    #a="BIENVENUE DANS HOME"
    #compagnie=Compagnie.objects.all()
    vol=Vol.objects.all()
    volid=Vol.objects.get(id=vol_d).compagnie_set.all()
    lng=len(volid)
    
    #message="{} est à {}.  ,  sa date de depart est le {}.à {} ".format(vol_d,compagnie.nom,compagnie.logo)
    #return HttpResponse(message)
    #a="bonjour"
    #vol=Vol

    #return HttpResponse(volid)
    return render(request,'listcom.html',locals())

def detail(request,vol_id):
    #a="bonjour tu as saisi",compagnie_id
    vol=Vol.objects.get(pk=vol_id)
    message="Le vol {} est à {}.  ,  sa date de depart est le {}.à {} ".format(vol_id,vol.prix,vol.date,vol.heure)


    return HttpResponse(message) 
    return render

