from rest_framework import serializers
from models import Autor

class AutorSerializar(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    pais = serializers.CharField(max_length=50)
    descripcion = serializers.CharField(max_length=200)
    foto = serializers.ImageField()

    def update(self, instance, validated_data):
        """
        Actualizacion y return de una instancia de Persona ya existente con los datos validados
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance

    def create(self, validated_data):
        return Autor.objects.create(**validated_data)