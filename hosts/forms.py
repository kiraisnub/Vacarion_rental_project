from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomHostUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username= forms.CharField(label="Username or Email",max_length=254)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.",code='inactive')

class CustomHostUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomHostUser
        fields=('username','email','first_name','last_name','Profile','City')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['Profile'].required = True
        self.fields['City'].required = True

class CustomHostUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomHostUser
        fields=('username','email','first_name','last_name','Profile','City')