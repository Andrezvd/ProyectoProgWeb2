from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib import messages
from .models import Personaje
from django.core.paginator import Paginator


from .forms import NewUserForm,crearPersonajeForm

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))


def clases(request):
    template = loader.get_template("clases.html")
    context = {}
    return HttpResponse(template.render(context,request))

def resumen(request):
    template =  loader.get_template("resumen.html")
    context = {}
    return HttpResponse(template.render(context,request))

def mundoabierto(request):
    template = loader.get_template("mundoabierto.html")
    context = {}
    return HttpResponse(template.render(context,request))

def jugabilidad(request):
    template = loader.get_template("jugabilidad.html")
    context = {}
    return HttpResponse(template.render(context,request))

def preguntas(request):
    template = loader.get_template("preguntas.html")
    context = {}
    return HttpResponse(template.render(context,request))

def gsotorneos(request):
    template = loader.get_template("gsotorneos.html")
    context = {}
    return HttpResponse(template.render(context,request))

def esports(request):
    template = loader.get_template("esports.html")
    context = {}
    return HttpResponse(template.render(context,request))

def ajustes(request):
    template = loader.get_template("ajustes.html")
    context = {}
    return HttpResponse(template.render(context,request))


def suscripcion(request):
    template = loader.get_template("suscripcion.html")
    context = {}
    return HttpResponse(template.render(context,request))

def jdestacados(request):
    
    personajes_list = Personaje.objects.all().order_by('-nivel')  # Ordenar por nivel descendente
    
    
    paginator = Paginator(personajes_list, 9)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("jdestacados.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def historia(request):
    template = loader.get_template("historia.html")
    context = {}
    return HttpResponse(template.render(context,request))

def descarga(request):
    template = loader.get_template("descargar.html")
    context = {}
    return HttpResponse(template.render(context,request))

def noticias(request):
    template = loader.get_template("noticias.html")
    context = {}
    return HttpResponse(template.render(context,request))



def personajes(request):
    try:
        personaje = request.user.personaje
        tiene_personaje = True
    except Personaje.DoesNotExist:
        tiene_personaje = False

    context = {
        'tiene_personaje': tiene_personaje,
        'personaje': personaje if tiene_personaje else None
    }

    return render(request, 'personajes.html', context)




def crearPersonaje(request):
    #Obtener el template
    template = loader.get_template("crearPersonaje.html")
    #Generar Formulario
    if request.method == "POST":
        form = crearPersonajeForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            Personaje_nuevo = form.save(commit=False)
            #Guardar personaje
            Personaje_nuevo.user=request.user
            Personaje_nuevo.save()
            return redirect('personajes')
    else:
        form = crearPersonajeForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))
