from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)