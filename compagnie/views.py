from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from reservation.models import Vol,Compagnie

# Create your views here.

def homecompagnie(request):
    #a="BIENVENUE DANS HOME"
    compagnie=Compagnie.objects.all()
    #a="bonjour"
    #vol=Vol

    #return HttpResponse(vol)
    return render(request,'homecompagnie.html',locals())

def detailcompagnie(request,compagnie_id):
    compagnie=Compagnie.objects.get(pk=compagnie_id)
    return render(request,'detailcompagnie.html',locals())