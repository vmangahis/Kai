from django.db import models
from import_export import resources
from django.contrib.auth.models import AbstractUser



class StudioCompany(models.Model):
    studio_name = models.CharField(max_length=60)
    anime_works = models.ManyToManyField('Anime', blank=True)

    def __str__(self):
        return self.studio_name

class AnimeGenre(models.Model):
    name = models.CharField(max_length=15, unique=True, default='Test')

    def __str__(self):
        return self.name

class MangaGenre(models.Model):
    name = models.CharField(max_length=15, unique=True, default='Test')

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=100, default=None, unique=True, null=True)
    premiere_date = models.DateField(default=None, blank=True, null=True)
    summary = models.TextField(default="No summary")
    genre = models.ManyToManyField(AnimeGenre)
    thumbnail = models.URLField(max_length=200, default="https://picsum.photos/seed/picsum/300/500", null=True)
    large_image = models.URLField(max_length=200, default="https://picsum.photos/seed/picsum/500/500", null=True)
    
    watchers = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, default=None, null=True)

    def __str__(self):
        return str(self.title)

class Manga(models.Model):
    title = models.CharField(max_length=100, default=None)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)
    summary = models.TextField(default="No summary")
    large_image = models.URLField(max_length=200, default="https://picsum.photos/seed/picsum/500/500")
    thumbnail = models.URLField(max_length=200, default="https://picsum.photos/seed/picsum/300/500")
    genre = models.ManyToManyField(MangaGenre)
    

    def __str__(self):
        return self.title

class UserWatchlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    status = models.ForeignKey('WatchlistStatus', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + ' ' + self.anime.title + ' STATUS:' + self.status.status_type)

class UserReadlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    status = models.ForeignKey('ReadlistStatus', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + ' ' + self.manga.title + ' STATUS:' + self.status.status_type)


class WatchlistStatus(models.Model):
    status_type = models.CharField(max_length=20)

    def __str__(self):
        return self.status_type

class ReadlistStatus(models.Model):
    status_type = models.CharField(max_length=20)

    def __str__(self):
        return self.status_type

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True, default='John Doe' ,blank=True, null=True)
    works = models.ManyToManyField(Manga, related_name='author_work', blank=True)


class User(AbstractUser):
    display_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=False)
    intro = models.TextField(null=True)

    
    
    

    
    
    

    avatar = models.ImageField(null=True, default='blank-avatar.svg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []





