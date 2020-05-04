from anvorguesa.models import Ingrediente,Hamburguesa
from anvorguesa.serializers import IngredienteSerializer,HamburguesaSerializer
from rest_framework import generics

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ingredientes': reverse('ingrediente-list', request=request, format=format),
        'hamburguesas': reverse('hamburguesa-list', request=request, format=format)
    })

@api_view(['GET','POST'])
def hamburguesa_list(request,format=None):
    serializer_context = {
        'request': request,
        }
    if request.method=='GET':
        hamb=Hamburguesa.objects.all()
        
        serializer=HamburguesaSerializer(hamb,many=True,context=serializer_context)
        # for h in Hamburguesa.objects.all():
        #     serializer.data[h.id]['ingredientes']='caca'
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=HamburguesaSerializer(data=request.data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PATCH'])
def hamburguesa_detail(request,pk,format=None):
    if request.method=='GET':
        if  not pk.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        try:
            ham=Hamburguesa.objects.get(pk=pk)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
        'request': request,
        }
        serializer = HamburguesaSerializer(ham,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if  not pk.isnumeric():
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            ham=Hamburguesa.objects.get(pk=pk)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ham.delete()
        return Response(status=status.HTTP_200_OK)
    
    elif request.method=='PATCH':
        
        try:
            ham=Hamburguesa.objects.get(pk=pk)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
        'request': request,
        }
        serializer=HamburguesaSerializer(ham,data=request.data,context=serializer_context,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def ingredient_to_hamburger(request, h_pk,i_pk, format=None):
    """
    Retrieve, update or delete a code ingrediente.
    """
    if  not (h_pk.isnumeric()):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        hamburguesa = Hamburguesa.objects.get(pk=h_pk)
    except Hamburguesa.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if  not (i_pk.isnumeric()):
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer_context = {
    'request': request,
    }
    if request.method == 'PUT':
        
        try:
            ingrediente = Ingrediente.objects.get(pk=i_pk)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hamburguesa.ingredientes.add(ingrediente)
        serializer = HamburguesaSerializer(hamburguesa,context=serializer_context)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        try:
            ingrediente=hamburguesa.ingredientes.get(pk=i_pk)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hamburguesa.ingredientes.remove(ingrediente)
    serializer = HamburguesaSerializer(hamburguesa,context=serializer_context)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def ingrediente_list(request, format=None):
    serializer_context = {
        'request': request,
        }
    if request.method=='GET':
        ingrediente=Ingrediente.objects.all()
        serializer=IngredienteSerializer(ingrediente,many=True,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='POST':
        serializer=IngredienteSerializer(data=request.data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
@api_view(['GET','DELETE'])
def ingrediente_detail(request,pk,format=None):
    if request.method=='GET':
        if not pk.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            ing=Ingrediente.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer_context = {
        'request': request,
        }
        serializer = IngredienteSerializer(ing,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        try:
            ing=Ingrediente.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        hams_con_ing=ing.hamburguesa_set.all()
        if hams_con_ing.exists():
            return Response(status=status.HTTP_409_CONFLICT) 
        ing.delete()
        return Response(status=status.HTTP_200_OK)




    
