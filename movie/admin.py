from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
class  GenreAdmin(admin.ModelAdmin):
    pass

class  MovieAdmin(admin.ModelAdmin):
    list_display = {'title', 'posted_by', 'show_from', 'show_until', 'created_at'}

    admin.site.register(Genre, GenreAdmin)
    admin.site.register(Movie, GenreAdmin)
