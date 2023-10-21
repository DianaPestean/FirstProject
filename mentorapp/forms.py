from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import  UserPlatform
from django.forms import TextInput, Textarea


class LogInForm(forms.Form):
    user_name = forms.CharField(max_length=60)
    user_password = forms.CharField(max_length=60, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
        ]
