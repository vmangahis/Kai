# Generated by Django 4.0.5 on 2022-10-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_anime_premiere_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(to='base.animegenre'),
        ),
        migrations.AddField(
            model_name='manga',
            name='genre',
            field=models.ManyToManyField(to='base.mangagenre'),
        ),
    ]