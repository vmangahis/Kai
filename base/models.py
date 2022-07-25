from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    diplay_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    intro = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='blank-avatar.svg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Anime(models.Model):
    pass