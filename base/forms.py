from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['display_name', 'username', 'email', 'password1', 'password2' ]

