# Generated by Django 4.0.5 on 2022-10-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_anime_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Test', max_length=15, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Genre',
            new_name='AnimeGenre',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='genre',
        ),
    ]
