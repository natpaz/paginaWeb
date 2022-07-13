from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .import views
from .views import ProductoList, ProductoCreate, ProductoUpdate , ProductoDelete, ProdList
 
urlpatterns = [
    path('listar_producto/', ProductoList.as_view(), name="listar_producto"),
    
    path('producto_form/', ProductoCreate.as_view(), name="producto_form"),
    
    path('editar_producto/<int:pk>', ProductoUpdate.as_view(), name="editar_producto"),
    
    path('borrar_producto/<int:pk>', ProductoDelete.as_view(), name="borrar_producto"),
    
    path('api/',  views.producto_collection , name='producto_collection'),
    
    path('api/<int:pk>', views.producto_element ,name='producto_element'),
    
    path('productos_venta/', ProdList.as_view(), name='productos_venta'),
    
    
]
