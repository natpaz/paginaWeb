from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FormularioSerializer
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import FormularioForm
from .models import Formulario
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your views here.
def listar_formulario(request):
    formularios = Formulario.objects.all()
    return render(request, "Formulario/listar_formulario.html", {'formularios': formularios})

def agregar_formulario(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("agregar_formulario")
    else:
        form = FormularioForm()
        return render(request, "agregar_formulario.html", {'form': form})
 
def borrar_formulario(request, formulario_id):
    # Recuperamos la instancia del formulario y la borramos
    instancia = Formulario.objects.get(id=formulario_id)
    instancia.delete()
 
    # Después redireccionamos de nuevo a la lista
    return redirect('listar_Formulario')
 
def editar_formulario(request, formulario_id):
    # Recuperamos la instancia de la formulario
    instancia = Formulario.objects.get(id=formulario_id)
 
    # Creamos el formulario con los datos de la instancia
    form = FormularioForm(instance=instancia)
 
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = FormularioForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
 
    # Si llegamos al final renderizamos el formulario
    return render(request, "editar_formulario.html", {'form': form})

class FormularioCreate(CreateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'Formulario/agregar_formulario.html'
    success_url = reverse_lazy("home")

class FormularioList(ListView):
    model = Formulario
    template_name = 'Formulario/listar_formulario.html'
    # paginate_by = 4

class FormularioUpdate(UpdateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'Formulario/agregar_formulario.html'
    success_url = reverse_lazy('listar_formulario')

        

class FormularioDelete(DeleteView):
    model = Formulario
    template_name = 'Formulario/borrar_formulario.html'
    success_url = reverse_lazy('listar_formulario')
    

# Aquí creamos la vista del API para poder hacer el get y el post de los formularios.
@api_view(['GET', 'POST'])
def formulario_collection(request):
    if request.method == 'GET':
        formularios = Formulario.objects.all()
        serializer = FormularioSerializer(formularios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FormularioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Acá abajo creamos la vista para tomar, ingresar, y borrar datos de la API.
@api_view(['GET', 'PUT', 'DELETE'])
def formulario_element(request, pk):
    formulario = get_object_or_404(Formulario, id=pk)

    if request.method == 'GET':
        serializer = FormularioSerializer(formulario)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        formulario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        formulario_new = JSONParser().parse(request) 
        serializer = FormularioSerializer(formulario, data=formulario_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


