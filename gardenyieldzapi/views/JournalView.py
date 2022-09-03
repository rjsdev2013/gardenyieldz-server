"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tomlkit import date
from gardenyieldzapi.models import Journal, Gardener, journal
from gardenyieldzapi.models.plant import Plant


class JournalView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)
        

    def list(self, request):
        journals = Journal.objects.all()
        serializer = PlantSerializer(journals, many=True)
        return Response(serializer.data)

class JournalSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Journal
        fields = ('id', 'date', 'fruitNumber', 'weight','plant_id','gardener_id')
        depth = 1
        
def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    gardener = Gardener.objects.get(user=request.auth.user)
    plant_id = Plant.objects.get(pk=request.data["plant_id"])

    journal = Journal.objects.create(
        date=request.data["date"],
        fruitNumber=request.data["fruitNumber"],
        weight=request.data["weight"],
        plant_id=request.data["plant_id"],
        gardener=gardener,
        plant_id=plant_id
    )
    serializer = JournalSerializer(journal)
    return Response(serializer.data)

# 8/30 added journalView create function;initiated git;next is edit and then delete(ch10)

def update(self, request, pk):
    """Handle PUT requests for a game

    Returns:
        Response -- Empty body with 204 status code
    """

    journal = Journal.objects.get(pk=pk)
    journal.date = request.data["date"]
    journal.fruitNumber = request.data["fruitNumber"]
    journal.weight = request.data["weight"]
    journal.plant_id = request.data["plant_id"]
    journal.gardener_id = request.data["gardener_id"]

    journal.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
