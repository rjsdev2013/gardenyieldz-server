"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tomlkit import date
from gardenyieldzapi.models import Journal, Gardener, journal
from gardenyieldzapi.models.plant import Plant


class JournalView(ViewSet):
    """Journals view"""

    def retrieve(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)
        

    def list(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        gardener = Gardener.objects.get(user=request.auth.user)
        plant_id = Plant.objects.get(pk=request.data["plant_id"])
        
    
        journal = Journal.objects.create(
            gardener = gardener,
            plant = plant_id,
            weight = request.data["weight"],
            fruitNumber = request.data["fruitNumber"]
        )
        
        serializer = CreateJournalSerializer(journal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game"""
        journal = Journal.objects.get(pk=pk)
        journal.fruitNumber = request.data["fruitNumber"]
        journal.weight = request.data["weight"]
        journal.plant_id = request.data["plant_id"]
        journal.gardener_id = request.data["gardener_id"]

        journal.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        journal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class JournalSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Journal
        fields = ('id', 'date', 'fruitNumber', 'weight','plant','gardener')
        depth = 1
        
class CreateJournalSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Journal
        fields = (
            'id',
            'fruitNumber',
            'weight',
            'plant',
            'gardener'   
        )