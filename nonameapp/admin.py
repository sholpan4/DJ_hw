from django.contrib import admin
from .models import Film, Genre


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'published', 'genre')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre)
