from rest_framework import serializers
from .models import SenosrInstance
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=SenosrInstance
        fields=['id','name']