# Generated by Django 4.0.5 on 2022-11-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_user_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='blank-avatar.jpg', null=True, upload_to=''),
        ),
    ]