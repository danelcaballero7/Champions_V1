from django import forms
from .models import Player
from django.contrib.auth.models import User


class player_form(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'last_name', 'age']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']