from django.urls import path
from .views import (PagInicio, 
                    devolverHoraServidor, 
                    CategoriasController, 
                    CategoriaController, 
                    Golosinascontroller,
                    GolosinaController)

urlpatterns = [
    path('inicio', PagInicio),
    path('status', devolverHoraServidor),
    path('categorias', CategoriasController.as_view()),
    path('categoria/<id>', CategoriaController.as_view()),
    path('golosinas', Golosinascontroller.as_view()),
    path('golosina/<id>', GolosinaController.as_view())
]
















