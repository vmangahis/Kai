from django.contrib import admin
from .models import StudioCompany, User, Anime, AnimeGenre, Manga, MangaGenre, Author
from import_export.admin import ImportExportModelAdmin
from import_export import resources




class AnimeResource(resources.ModelResource):
    class Meta:
        model = Anime
        exclude = ('premiere_date', 'genre')

class  AnimeGenreResource(resources.ModelResource):
    class Meta:
        model = AnimeGenre
        

class MangaGenreResource(resources.ModelResource):
    class Meta:
        model = MangaGenre


class MangaResource(resources.ModelResource):
    class Meta:
        model = Manga
        exclude=('author', 'genre',)
        

class AnimeResourceAdmin(ImportExportModelAdmin):
    resource_class = AnimeResource



class MangaResourceAdmin(ImportExportModelAdmin):
    resource_class = MangaResource

class AnimeGenreResourceAdmin(ImportExportModelAdmin):
    resource_class = AnimeGenreResource

class MangaGenreResourceAdmin(ImportExportModelAdmin):
    resource_class = MangaGenreResource






admin.site.register(User)
admin.site.register(Anime, AnimeResourceAdmin)
admin.site.register(AnimeGenre, AnimeGenreResourceAdmin)
admin.site.register(MangaGenre, MangaGenreResourceAdmin)
admin.site.register(Manga, MangaResourceAdmin)
admin.site.register(Author)
admin.site.register(StudioCompany)
