from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

#
from rest_framework.response import Response
from rest_framework import status

class ProductoView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request):
        print(self.get_queryset())
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'ok': True,
            'content':respuesta.data,
            'message': None
        })
    
    def post(self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=False):
            # con el save se hace el guardado a la base de datos
            respuesta.save()
            return Response({
                'ok':True,
                'content':respuesta.data,
                'message':None
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'ok':False,
                'content':None,
                'message':'Hubo un error al crear'
            },status=status.HTTP_400_BAD_REQUEST)