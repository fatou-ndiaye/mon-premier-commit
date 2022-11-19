from django.http import HttpResponse
from django.shortcuts import render

from .models import Compagnie


# Create your views here.
def home(request):
    #a="Fatou"
    #return HttpResponse(a)
    return render(request,"home/home.html",locals())


def compagnie_view(request):
    
        # récupération du contenu
        compagnie = Compagnie.objects.all()
        #context:{'compagnie':compagnie}     
        return render(request, "DEMO/home.html")   
        #return HttpResponse(compagnie)
     