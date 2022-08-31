from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    plant_date= models.IntegerField(null=True)