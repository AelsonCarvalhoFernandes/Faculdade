from rest_framework import serializers
from .models import Funcionarios

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = ['__all__']