from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    diplay_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=False)
    intro = models.TextField(null=True)


    avatar = models.ImageField(null=True, default='blank-avatar.svg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True, default='Test')

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=100, default=None, unique=True)
    premiere_date = models.DateField(default=None)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Manga(models.Model):
    title = models.CharField(max_length=100, default=None)
    author = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title





