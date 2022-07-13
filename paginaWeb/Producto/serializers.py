from rest_framework import serializers
from .models import Producto

# Acá creamos el serializers para enviar los datos del formulario a la API.
class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id','codigo', 'nombre', 'precio', 'imagen')
