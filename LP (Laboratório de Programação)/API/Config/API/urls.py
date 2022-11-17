from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Funcionario', views.FuncionariosViewSets)

urlpatterns = [

    path('', include(router.urls)),
]
