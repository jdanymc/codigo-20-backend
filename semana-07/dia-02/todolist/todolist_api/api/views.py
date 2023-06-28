from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import Tarea
from .serializers import TareaSerializer

class IndexView(APIView):
    def get(self, request):
        context = {
            'status': True,
            'content': 'Servidor Activo'
        }
        return Response(context)

class TareaView(APIView): # TareaView hereda de APIView
    def get(self, request):
        data = Tarea.objects.all()
        serializer = TareaSerializer(data, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class TareaDetailView(APIView): # solo se expone get, post, put, delete
    def get_object(self, pk):
        try:
            return Tarea.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        data = self.get_object(pk)
        serialiazer = TareaSerializer(data)
        return Response(serialiazer.data)
    
    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = TareaSerializer(data, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400
    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204
