from rest_framework import serializers
from anvorguesa.models import Hamburguesa,Ingrediente
from django.forms.models import model_to_dict

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Ingrediente
        fields=('url','id','nombre','descripcion')

class IngEnHAmburguesaSerializer(serializers.Serializer):
    class Meta:
        model=Ingrediente
        fields=('id',)

class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes=IngEnHAmburguesaSerializer
    class Meta:
        model=Hamburguesa
        fields=('url','id','nombre','precio','descripcion','img','ingredientes')

    def to_representation(self,instance):
        result = dict()
        
        ing_list=[]
        # result["url"]=instance.url
        result["id"]=instance.id
        result["nombre"]=instance.nombre
        result["precio"]=instance.precio
        result["descripcion"]=instance.descripcion
        result["img"]=instance.img
        for ingrediente in instance.ingredientes.all():
            ings=dict()
            ings["path"]="https://anvorguesaapp.herokuapp.com/{}".format(ingrediente.id)
            ing_list.append(ings)
        result["ingredientes"]=ing_list
        return result




## Sin hyperlink
# class IngredienteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Ingrediente
#         fields=['id','nombre','descripcion']


# class HamburguesaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hamburguesa
#         fields=['id','nombre','precio','descripcion','img','ingredientes']



