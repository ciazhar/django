Tutorial Django

setup environment
  install python 3

  pip install djanggo
  Note : pastikan install python-pip

bikin project
  django-admin startproject tutorial_bioskop
  NOte : pastikan install python-django-common

add project ke text editor

migrate database, secara default dia pake SQLite:
  python manage.py migrate

bikin superuser
  python manage.py createsuperuser

jalankan aplikasi :
  python manage.py runserver

aplikasi di browser :
  localhost:8000
  Note : buat accsess admin localhost:8000/admin, kalo mau ganti di urls.py

bikin apps :
  python manage.py startapp movie

bikin model (models.py):
  from __future__ import unicode_literals

  from django.db import models
  from django.contrib.auth.models import User

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

setting app (settings.py)
  'movie' ke INSTALLED_APPS


migrasi database :
  python manage.py makemigration
  python manage.py migrate

setting admin(admin.py)
  from django.contrib import admin
  from .models import Genre, Movie

  # Register your models here.
  class  GenreAdmin(admin.ModelAdmin):
      pass

  class  MovieAdmin(admin,ModelAdmin):
      list_display = {'title', 'posted_by', 'show_from', 'show_until', 'created_at'}

      admin.site.register(Genre, GenreAdmin)
      admin.site.register(Movie, GenreAdmin)
