from rest_framework import serializers
from models import Question

class QuestionSerializar(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    asunt = serializers.CharField(max_length=200)
    descrip = serializers.CharField()
    date = serializers.CharField()

    def update(self, instance, validated_data):
        """
        Actualizacion y return de una instancia de Persona ya existente con los datos validados
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.asunt = validated_data.get('asunt', instance.asunt)
        instance.descrip = validated_data.get('descrip', instance.descrip)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    def create(self, validated_data):
        return Question.objects.create(**validated_data)