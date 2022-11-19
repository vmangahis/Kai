import cloudinary
from django.apps import AppConfig
from decouple import config



class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    def ready(self):
        cloudinary.config(
            cloud_name = config("CLOUDINARY_NAME"),
            api_key = config("CLOUDINARY_API_KEY"),
            api_secret = config("CLOUDINARY_SECRET_API")
        )
