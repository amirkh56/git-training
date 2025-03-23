from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PerosnSerializer
# from rest_framework.permissions import 


class Home (APIView) :
    permission_classes = []

    
    def get(self, request) :
        person = Person.objects.all()
        ser_data = PerosnSerializer(instance = person, many=True)
        return Response(data = ser_data.data)
    
