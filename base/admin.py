from django.contrib import admin
from .models import User, Anime, Genre, Manga

admin.site.register(User)
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Manga)