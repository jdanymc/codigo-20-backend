from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from api.models import (
    Mesa, Categoria, Plato
)

from api.serializers import(
    MesaSerializer, CategoriaSerializer, PlatoSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

""" vista para subir imagenes"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader

class UploadPlatoImageView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser
    )

    @staticmethod
    def post(request):
        file = request.data.get('plato_img')

        upload_data=cloudinary.uploader.upload(file)

        return Response(upload_data, status=201)