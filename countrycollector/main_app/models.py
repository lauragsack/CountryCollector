from django.db import models
from django.urls import reverse

RIVERS = (
    ('D', 'Danube'), 
    ('E', 'Elbe'),  
    ('R', 'Rhone')
    )
# Create your models here.
class RiverCruise(models.Model):
    name = models.CharField(max_length=100)
    river = models.CharField(
        max_length=1,
        choices=RIVERS,
        default=RIVERS[0][0]
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cruises_detail', kwargs={'pk': self.id})

class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    visited = models.BooleanField()
    cruises = models.ManyToManyField(RiverCruise)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    visited = models.BooleanField()
    what_to_eat = models.TextField(max_length=250)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
