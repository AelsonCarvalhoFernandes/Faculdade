from rest_framework import viewsets
from .models import Funcionarios
from .serializer import FuncionarioSerializer

class FuncionariosViewSets(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionarioSerializer
    



