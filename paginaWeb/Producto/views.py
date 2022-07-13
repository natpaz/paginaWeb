from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductoForm
from .models import Producto
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from .models import Producto
from .forms import ProductoForm
# Create your views here.

class ProductoList (ListView):                    
    model = Producto
    template_name = 'Producto/listar_producto.html'

class ProductoCreate (CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/producto_form.html'
    success_url = reverse_lazy('listar_producto')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/producto_form.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Producto/borrar_producto.html'
    success_url = reverse_lazy('listar_producto')
    
class ProdList (ListView):                    
    model = Producto
    template_name = 'Producto/productos_venta.html'


@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Acá abajo creamos la vista para tomar, ingresar, y borrar datos de la API.
@api_view(['GET', 'PUT', 'DELETE'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        producto_new = JSONParser().parse(request) 
        serializer = ProductoSerializer(producto, data=producto_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
