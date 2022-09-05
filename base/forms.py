from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

from .models import User

class UserCreation(UserCreationForm):

    tos = forms.BooleanField(required=False, label=mark_safe("I agree to <a href='#'><u>Terms of Service</u></a> "))
    class Meta:
        model = User
        fields = ['display_name', 'username', 'email', 'password1', 'password2', 'tos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['display_name'].widget.attrs['class']="form-control display-name-reg"
        self.fields['display_name'].widget.attrs['placeholder']="Display Name"
        #self.fields['display_name'].widget.attrs['name']="display-name-reg"
        #self.fields['display_name'].widget.attrs['id']="display-name-reg"

        

        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['username'].widget.attrs['placeholder']="Username"
        self.fields['username'].widget.attrs['autofocus']=False

        self.fields['email'].widget.attrs['class']="form-control"
        self.fields['email'].widget.attrs['placeholder']="Email Address"

        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['placeholder']="Password"

        self.fields['password2'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['placeholder']="Confirm Password"

    def clean_password2(self):
        password_a = self.cleaned_data.get('password1')
        password_b = self.cleaned_data.get('password2')

        if password_a != password_b:
            raise forms.ValidationError('Password does not match to each other')

        return password_a

    def clean_email(self):
        email = self.cleaned_data['email']
        if(User.objects.filter(email__iexact=email)).exists():
            raise forms.ValidationError('Email already exists.')

        return email

    def clean_tos(self):
        tosCheck = self.cleaned_data['tos']
        if tosCheck is False:
            raise forms.ValidationError(mark_safe('You must agree to our <a href="#"><u>Terms of Service</u></a>'))

        return tosCheck


    
    
