from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Alumno
from .serializers import AlumnoSerializer

@api_view(['GET'])
def index(request):
    context = {
        'status': True,
        'content': 'API rest con DRF'
    }

    return Response(context) # se convierte a json y retorna

@api_view(['GET','POST'])
def alumno(request):
    if request.method == 'GET':
        lista_alumnos = Alumno.objects.all()
        ser_alumnos = AlumnoSerializer(lista_alumnos, many=True)
        context = {
            'status': True,
            'content': ser_alumnos.data,
        }
    elif request.method == 'POST':
        ser_alumno = AlumnoSerializer(data=request.data)
        ser_alumno.is_valid(raise_exception=True)

        obj_nuevo_alumno = ser_alumno.save()

        context = {
            'status': True,
            'content': AlumnoSerializer(obj_nuevo_alumno).data,
        } 
    return Response(context)