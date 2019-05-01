from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    Registration form that extends from the built-in UserCreationForm

    """
    email = forms.Field()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']