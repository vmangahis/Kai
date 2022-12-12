from django import forms
from django.forms import ModelForm, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

from .models import User



def val_username_char(username):
        for ch in username:
            if not ch.isdigit() and not ch.isalpha():
                return False
                
        return True


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

    def clean_username(self):
        user = self.cleaned_data['username']

        if not val_username_char(user):
            raise forms.ValidationError("Username must only numbers and letters.")

        return user

    def clean_tos(self):
        tosCheck = self.cleaned_data['tos']
        if tosCheck is False:
            raise forms.ValidationError(mark_safe('You must agree to our <a href="#"><u>Terms of Service</u></a>'))

        return tosCheck


class UserEditForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['display_name', 'intro', 'avatar']
        widgets = {
            'avatar': FileInput
            }
    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['display_name'].required = True
        self.fields['intro'].required = False
        self.fields['intro'].label = "Introduction"
        self.fields['display_name'].label = "Display Name"
        self.fields['display_name'].widget.attrs.update({
            'class': 'form-control displayname-input-edit'
        })
        self.fields['intro'].widget.attrs.update({
            'class': 'form-control bio-textarea'
        })
        
    

    def clean_display_name(self):
        dName = self.cleaned_data['display_name']
        return dName

    #def clean_avatar

    
    def clean_intro(self):
        bio = self.cleaned_data['intro']

        # in case user inputs blank bio
        if bio == "" or bio.isspace():
            bio = "No summary."

        return bio




    
