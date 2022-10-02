from django.contrib import admin
from .models import StudioCompany, User, Anime, Genre, Manga, Author
from import_export.admin import ImportExportModelAdmin
from import_export import resources



class AnimeResource(resources.ModelResource):
    class Meta:
        model = Anime
        field = ('id', 'title', 'thumbnail')

class AnimeResourceAdmin(ImportExportModelAdmin):

    resource_class = AnimeResource


admin.site.register(User)
admin.site.register(Anime, AnimeResourceAdmin)
admin.site.register(Genre)
admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(StudioCompany)

