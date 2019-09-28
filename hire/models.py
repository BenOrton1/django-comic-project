from django.db import models

# Create your models here.
LINEART = 'Line art only'
BLACKANDWHITE = 'Black and white'
FULLCOLOUR = 'Full colour'
YES='Yes'
NO='No'

in_colour = [
    (LINEART, 'Line art only'),
    (BLACKANDWHITE, 'Black and white'), 
    (FULLCOLOUR, 'Full colour')]
boolian=[
    (YES, 'Yes'),
    (NO, 'No')
    ]

    


class Commition(models.Model):
    yourname = models.CharField(max_length=40, default='Name')
    colour = models.CharField(max_length=40,
                              choices=in_colour,
                              default=LINEART)
    cover = models.CharField(max_length=40,
                              choices=boolian,
                              default=NO)
    setting = models.CharField(max_length=40, blank=False)
    number_of_characters = models.IntegerField()
    number_of_pages = models.IntegerField()
    deadline = models.DateField(blank=False)
    email = models.EmailField(blank=False)
