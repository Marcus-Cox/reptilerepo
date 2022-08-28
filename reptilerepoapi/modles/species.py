from django.db import models


class ReptileSpecies(models.Model):

    species = models.CharField(max_length=50)
