# Generated by Django 4.0.5 on 2022-12-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_activities_title_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='activity_thumbnail',
            field=models.URLField(default='https://via.placeholder.com/150'),
        ),
    ]
