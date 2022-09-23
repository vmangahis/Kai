from django.contrib import admin
from .models import StudioCompany, User, Anime, Genre, Manga, Author

admin.site.register(User)
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(StudioCompany)