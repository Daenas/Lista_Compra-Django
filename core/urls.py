from django.urls import path
from .views import index, processa_formulario

urlpatterns = [
    path("", index, name = "index"),
    path("processa_formulario", processa_formulario, name = "processa_formulario")
]