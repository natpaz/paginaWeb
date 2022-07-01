from rest_framework import serializers
from .models import Formulario

# Acá creamos el serializers para enviar los datos del formulario a la API.
class FormularioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Formulario
        fields = ('id','nombre', 'asunto', 'correo', 'mensaje')
