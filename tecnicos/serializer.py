from rest_framework import serializers
from .models import *

# Serializers define the API representation.


class TecnicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnicos
        fields = '__all__'


class TiposOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposOS
        fields = '__all__'


class TecnicosMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicosMensagem
        fields = '__all__'
        


class TempoSLASerializer(serializers.ModelSerializer):
    class Meta:
        model = TempoSLA
        fields = '__all__'


class SLA_OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SLA_OS
        fields = '__all__'


class InformacoesOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesOS
        fields = '__all__'


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
