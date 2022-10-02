from django.contrib import admin
from .models import StudioCompany, User, Anime, Genre, Manga, Author
from import_export.admin import ImportExportModelAdmin
from import_export import resources, widgets, fields




class AnimeResource(resources.ModelResource):
    class Meta:
        model = Anime
        exclude = ('premiere_date', 'genre')

class AnimeResourceAdmin(ImportExportModelAdmin):
    resource_class = AnimeResource

class MangaResource(resources.ModelResource):
    class Meta:
        model = Manga
        exclude=('author', 'genre',)
        

class MangaResourceAdmin(ImportExportModelAdmin):
    resource_class = MangaResource




admin.site.register(User)
admin.site.register(Anime, AnimeResourceAdmin)
admin.site.register(Genre)
admin.site.register(Manga, MangaResourceAdmin)
admin.site.register(Author)
admin.site.register(StudioCompany)

