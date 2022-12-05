from django.contrib import admin
from django.db import models
from .models import Activities,ActivityStatus, ActivityType, StudioCompany, User, Anime, AnimeGenre, Manga, MangaGenre, Author, UserWatchlist, WatchlistStatus, ReadlistStatus, UserReadlist
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
    list_display = ['title', 'premiere_date']
    resource_class = AnimeResource



class MangaResourceAdmin(ImportExportModelAdmin):
    resource_class = MangaResource

class AnimeGenreResourceAdmin(ImportExportModelAdmin):
    resource_class = AnimeGenreResource

class MangaGenreResourceAdmin(ImportExportModelAdmin):
    resource_class = MangaGenreResource

class UserWatchlistAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'created', 'updated_at']

    def get_user(self, obj):
        return obj.user.username

    get_user.short_description = "Username"




admin.site.register(User)
admin.site.register(Anime, AnimeResourceAdmin)
admin.site.register(ActivityStatus)
admin.site.register(AnimeGenre, AnimeGenreResourceAdmin)
admin.site.register(MangaGenre, MangaGenreResourceAdmin)
admin.site.register(Manga, MangaResourceAdmin)
admin.site.register(Author)
admin.site.register(StudioCompany)
admin.site.register(UserWatchlist, UserWatchlistAdmin)
admin.site.register(WatchlistStatus)
admin.site.register(ReadlistStatus)
admin.site.register(UserReadlist)
admin.site.register(Activities)
admin.site.register(ActivityType)
