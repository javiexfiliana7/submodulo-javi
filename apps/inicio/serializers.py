from rest_framework import serializers
from models import Perfiles

class PerfilesSerializar(serializers.Serializer):
    usuario = serializers.CharField(max_length=50)
    telefono = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        """
        Actualizacion y return de una instancia de Persona ya existente con los datos validados
        """
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance

    def create(self, validated_data):
        return Perfiles.objects.create(**validated_data)