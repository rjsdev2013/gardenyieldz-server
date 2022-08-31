"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gardenyieldzapi.models import Plant


class PlantView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        plant = Plant.objects.get(pk=pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
        

    def list(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

class PlantSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Plant
        fields = ('id', 'name', 'description', 'plant_date')
        depth = 1