from django.db import models

# Create your models here.
class Thing(models.Model):
    stuff = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
