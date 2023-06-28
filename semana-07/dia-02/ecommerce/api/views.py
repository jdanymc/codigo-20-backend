from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from web.models import Categoria, Producto, Marca
from .serializers import ( CategoriaSerializer, ProductoSerializer,
MarcaSerializer, CategoriaProductoSerializer, MarcaProductoSerializer)

class CategoriaView(generics.ListCreateAPIView): # TareaView hereda de APIView
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView): # TareaView hereda de APIView
    queryset = Categoria.objects.all()
    lookup_field = 'pk'
    serializer_class = CategoriaSerializer

class MarcaView(generics.ListCreateAPIView): # TareaView hereda de APIView
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetailView(generics.RetrieveUpdateDestroyAPIView): # TareaView hereda de APIView
    queryset = Marca.objects.all()
    lookup_field = 'pk'
    serializer_class = MarcaSerializer

class ProductoView(generics.ListCreateAPIView): # TareaView hereda de APIView
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaProductosView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaProductoSerializer

class MarcaProductosView(generics.RetrieveAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaProductoSerializer