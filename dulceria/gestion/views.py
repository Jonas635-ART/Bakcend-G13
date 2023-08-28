from math import ceil
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel, GolosinaModel
from .serializers import (CategoriaSerializer, 
                          GolosinaSerializer,
                          GolosinaResponseSerializer, 
                          CategoriaResponseSerializer)
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
        serializador = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            'message': 'La categoria es',
            'content': serializador.data
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

class CategoriaController(APIView):
    def get(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Catgeoria no encotrada'
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = CategoriaResponseSerializer(instance=categoriaEncontrada)
        return Response(data={
            'content': serializador.data
        })
    def put(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Catgeoria no encotrada'
            }, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializador = CategoriaSerializer(data=data)
        dataValida = serializador.is_valid()
        if dataValida:
            serializador.validated_data
            serializador.update(categoriaEncontrada,
                                serializador.validated_data)
            return Response(data={
                'message': 'Catgeoria actualizada'
            })
        else:
            return Response(data={
                'message': 'Error al actualizar',
                'content':serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Catgeoria no encotrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        CategoriaModel.objects.filter(id=id).delete()

        return Response(data={
            'message': 'Catgeoria eliminada'
        })

class Golosinascontroller(APIView):
    def get(self, request: Request):
        #totalgolosinas = GolosinaModel.objects.count()
        #print(request.query_params)# -> Para definir los query params

        page = int(request.query_params.get('page', 1))
        perPage = int(request.query_params.get('perPage',5))
        ordering = request.query_params.get('ordering')
        orderingType = request.query_params.get('orderingType')  # asc | desc
        # order_by('-nombre') > ordenar de manera descendente por la columna nombre
        #orderingType = '' if orderingType == 'asc' else '-' ordenar de forma ascendente
        orderingType = '-' if orderingType == 'desc' else ''

        # if (request.query_params.get('page') and request.query_params.get('perPage')):
        #     page = request.query_params.get(page)
        #     perPage = request.query_params.get(perPage)
        #     pass # -> Si no sabemos que sigue pero que no halla errores colocamos el pass
        # else:
        #     return Response(data={

        #     })
        skip = (page - 1) * perPage
        take = perPage * page

        if ordering:
            golosinas = GolosinaModel.objects.order_by(orderingType + ordering).all()[
                skip:take]
        else:
            golosinas = GolosinaModel.objects.all()[skip:take]

        totalGolosinas = GolosinaModel.objects.count()

        serializador = GolosinaSerializer(instance=golosinas, many=True)

        pagination = helperPagination(totalGolosinas, page, perPage)

        return Response(data={
            'content': serializador.data,
            'pagination': pagination
        })
class GolosinaController(APIView):
    def get(self, request: Request, id: str):
        golosinaEncontrada = GolosinaModel.objects.filter(id=id).first()
        if golosinaEncontrada is None:
            return Response(data={
                'message': 'La golosina no existe'
            }, status=status.HTTP_404_NOT_FOUND)

        print(golosinaEncontrada.categoria.nivelAzucar)
        serializador = GolosinaResponseSerializer(instance=golosinaEncontrada)

        return Response(data={
            'content': serializador.data
        })

def helperPagination(total: int, page: int, perPage: int):
    itemsPerPage = perPage if total >= perPage else total
    totalPages = ceil(total / itemsPerPage) if itemsPerPage > 0 else None
    prevPage = page - 1 if page > 1 and page <= totalPages else None
    nextPage = page + 1 if totalPages > 1 and page < totalPages else None

    return {
        'itemsPerPage': itemsPerPage,
        'totalPages': totalPages,
        'prevPage': prevPage,
        'nextPage': nextPage
    }


















