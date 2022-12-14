from tkinter import CASCADE
from django.db import models
from .lister import ReptileUser
from .species import ReptileSpecies


class ReptileListing(models.Model):
    lister = models.ForeignKey(ReptileUser, on_delete=models.CASCADE)
    species = models.ForeignKey(ReptileSpecies, on_delete=models.CASCADE)
    sex = models.CharField(max_length=50)
    morph = models.CharField(max_length=50)
    age = models.IntegerField()
    listing_date = models.DateField(auto_now_add=True)
    hatch_date = models.DateField(max_length=50)
    diet = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
