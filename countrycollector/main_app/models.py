from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    visited = models.BooleanField()

    def __str__(self):
        return self.name