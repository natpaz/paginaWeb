
from django.urls import path, include
from .import views
from django.contrib.auth.views import login_required
 
urlpatterns = [
 

  # llamando a la clases 
    path('agregar_formulario', views.FormularioCreate.as_view(), name="agregar_formulario"),
 
    path('listar_formulario', views.FormularioList.as_view(), name='listar_formulario'),
 
    path('editar_formulario/<int:pk>', (views.FormularioUpdate.as_view()), name='editar_formulario'),
 
    path('borrar_formulario/<int:pk>', (views.FormularioDelete.as_view()), name='borrar_formulario'),
    
    path('edit_formulario/<int:pk>', views.FormularioUpdate.as_view(), name='editar_formulario'),

    path('del_formulario/<int:pk>', views.FormularioDelete.as_view(), name='borrar_formulario'),
    
    path('api/',  views.formulario_collection , name='formulario_collection'),
    
    path('api/<int:pk>', views.formulario_element ,name='formulario_element'),
    
    path('add_formulario', views.FormularioCreate.as_view(), name="add_formulario"),


]


