from django.http import HttpResponse
from django.template import loader


# Create your views here.

def ajustes(request):
    template = loader.get_template("ajustes.html")
    context = {}
    return HttpResponse(template.render(context,request))


def suscripcion(request):
    template = loader.get_template("suscripcion.html")
    context = {}
    return HttpResponse(template.render(context,request))