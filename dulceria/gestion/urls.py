from django.urls import path
from .views import PagInicio, devolverHoraServidor, CategoriasController

urlpatterns = [
    path('inicio', PagInicio),
    path('status', devolverHoraServidor),
    path('categorias', CategoriasController.as_view()),
]
















