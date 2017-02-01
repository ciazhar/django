from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
class  GenreAdmin(admin.ModelAdmin):
    pass

class  MovieAdmin(admin.ModelAdmin):
    #yang ditampilkan di movie
    list_display = ('title','show_genres', 'posted_by', 'show_from', 'show_until', 'created_at', 'show_status')

    #yang ditampilan di form
    fields = ('title','description', 'show_from', 'show_until', 'genres')

    #otomatisasi save posted by
    def save_model(self, request, obj, form, change):
        obj.posted_by = request.user
        super(MovieAdmin, self).save_model(request,obj,form, change)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
