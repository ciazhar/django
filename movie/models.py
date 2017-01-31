from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Genre(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    #toString pyton 3
    def __str__(self):
        return self.title

    #toString pyton 2
    def __unicode__(self):
        return self.title


class  Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    show_from = models.DateField()
    show_until = models.DateField()
    genres = models.ManyToManyField(Genre)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #toString pyton 3
    def __str__(self):
        return self.title
    #toString pyton 2
    def __unicode__(self):
        return self.title
