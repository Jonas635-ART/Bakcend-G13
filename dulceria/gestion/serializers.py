from rest_framework import serializers
from .models import CategoriaModel, GolosinaModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
        #fields = ['id', 'nombre', 'nivelAzucar']
        #si quieres utilizar todos los atributos menos a uno o la minoria
        # exclude= ['id']

class GolosinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolosinaModel
        fields = '__all__'
class GolosinaResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolosinaModel
        fields = '__all__'
        # depth sirve para indicar cuantos niveles queremos recorrer cuyo valor maximo es 10
        depth = 1


class CategoriaResponseSerializer(serializers.ModelSerializer):
    # si queremos cambiar el nombre de nuestro related_name seteado en la relacion entre las tablas, podemos utilizar el parametro source, para indicar que parametro le pasaremos al serializador para que haga match, NOTA: no se puede usar el parametro source si el nombre del atributo es el mismo
    golosinass = GolosinaSerializer(many=True, source='golosinas')

    class Meta:
        model = CategoriaModel
        fields = '__all__'
        # no se tiene en este modelo la llave foranea no se puede usar el atributo depth
        # depth = 9




























