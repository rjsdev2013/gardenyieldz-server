from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Gardener(models.Model):
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)