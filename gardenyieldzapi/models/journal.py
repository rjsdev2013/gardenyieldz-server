from django.db import models
from django.contrib.auth.models import User
from gardenyieldzapi.models.plant import Plant
from gardenyieldzapi.models.gardener import Gardener



class Journal(models.Model):

# do I do a .ManyToManyField() or in the plant and gardener models?
    gardener = models.ForeignKey(Gardener, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    date = models.DateField(null=True)
    fruitNumber = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)