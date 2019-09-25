from django.db import models

# Create your models here.

class Commition(models.Model):
    colour = models.BooleanField(blank=False)
    cover = models.BooleanField(blank=False)
    setting = models.CharField(max_length=40, blank=False)
    number_of_characters = models.IntegerField()
    number_of_pages = models.IntegerField()
    deadline = models.DateField(blank=False)
    email = models.EmailField(blank=False)

