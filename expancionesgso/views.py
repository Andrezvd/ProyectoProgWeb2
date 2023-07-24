from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import ExpancionForm
from .models import Expancion
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your views here.

def expancionIndex(request):
    
    #Consultar expanciones
    expanciones_list = Expancion.objects.all()
    #Configurar paginación cada 9 expanciones
    paginator = Paginator(expanciones_list, 9)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("expancion.html")
    #Agregar el contexto
    context = {"page_obj":page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def compraExpancion(request, id):
    # Obtener el producto que se va a comprar
    user_coins = request.user.galaxyCoins
    #Obtener el template
    template = loader.get_template("compraExpanciones.html")
    #Buscar Producto
    obj = get_object_or_404(Expancion, id = id)

    expancion_precio = obj.precio
    #formulario que contiene la instancia
    if request.method == "POST":
        if user_coins >= expancion_precio:
            request.user.galaxyCoins -= expancion_precio
            request.user.save()
            return redirect('expancionIndex')
        else:
            return HttpResponse("SALDO INSUFICIENTE")
        #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))


# Vista principal de Gestión de expanciones
def gestionExpanciones(request):
    #Consultar expanciones
    expancion_list = Expancion.objects.all()
    #Configurar paginación cada 10 expanciones
    paginator = Paginator(expancion_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    #Obtener el template
    template = loader.get_template("gestionExpancion.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista para crear Expanciones
def crearExpancion(request):
    #Obtener el template
    template = loader.get_template("crearExpancion.html")
    #Generar Formulario
    if request.method == "POST":
        form = ExpancionForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            producto_nuevo.fecha_creacion = datetime.now()
            #Guardar Producto
            producto_nuevo.save()
            return redirect('gestionExpancion')
    else:
        form = ExpancionForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Expancion
def editarExpancion(request,id):
    #Obtener el template
    template = loader.get_template("editarExpancion.html")
    #Buscar Expancion
    obj = get_object_or_404(Expancion, id = id)
    #formulario que contiene la instancia
    form = ExpancionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('gestionExpancion')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Expanciones
def eliminarExpancion(request,id):
    #Obtener el template
    template = loader.get_template("eliminarExpancion.html")
    #Buscar el producto
    obj = get_object_or_404(Expancion, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('gestionExpancion')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))



