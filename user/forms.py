from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('email','username','age')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('email','username','age')
