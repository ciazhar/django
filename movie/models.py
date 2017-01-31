from __future__ import unicode_literals

from django.db import models

# Create your models here.

class  Genre(object):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

class  movie(object):
    title = models.Charfield(max_length=200)
    description = models.TextField(null=True, blank=True)
    show_from = models.DateField()
    show_until = models.DateField()
    genres = models.ManyToManyField(Genre)
    posted_by = models.ForeignKey(user)
    created_at = models.DataField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
