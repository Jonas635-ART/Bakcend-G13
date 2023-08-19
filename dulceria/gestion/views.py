from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework import status

# Ejemplo para renderizar plantillas.

def PagInicio(request):
    print(request)
    data = {
        'usuario': {
            'nombre': 'Fernado',
            'apellido':'Kolaris'
        },
        'hobbies': [
            {
                'descripcion': 'Ir al Gym'
            },
            {
                'descripcion':'Ir a la playa'
            }
        ]
    }
    
    return render(request, 'inicio.html', {'data': data}) #-> pasamos la data como diccionario

@api_view(http_method_names=['GET', 'POST'])
def devolverHoraServidor(request: Request):
    print(request.method)

    if request.method == 'GET':
        return Response(data= {
            'content': datetime.now()
        })
    elif request.method == 'POST':
        return Response(data= {
            'content': 'Para saber la hora usa el GET'
        })

class CategoriasController(APIView):
    def get(self, request: Request):
        categorias = CategoriaModel.objects.all()
        print(categorias)

        return Response(data={
            'message': 'La categoria es'
        })

    def post(self, request: Request):
        #donde se guarda la info proveniente del cliente
        data = request.data
        serializador = CategoriaSerializer(data=data)

        validacion = serializador.is_valid()
        if validacion == True:
            nuevaCategoria = serializador.save()
            print(nuevaCategoria)

            return Response(data={
                'message': 'Categoria creada'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)























