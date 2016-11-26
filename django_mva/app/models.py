from __future__ import unicode_literals

from django.db import models
import floppyforms as forms

# Create your models here.
class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()

class Album(models.Model):
    name = models.CharField("album", max_length=50)
    artist = models.ForeignKey(Artist)

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'year_formed']