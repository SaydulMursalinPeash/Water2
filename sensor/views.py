from django.shortcuts import render
from .models import SenosrInstance
from rest_framework.views import APIView,Response,status
from .serializers import SensorSerializer
def home(request):
    return render(request,'home.html')

class GetSensors(APIView):
    def get(self,request):
        sensors=SenosrInstance.objects.all().order_by('-time').first()
        serializer=SensorSerializer(sensors)
        return Response({"data":serializer.data()},status=status.HTTP_200_OK)
        
