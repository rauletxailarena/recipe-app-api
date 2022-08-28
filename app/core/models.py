from django.db import models
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title