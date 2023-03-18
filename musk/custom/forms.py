from dataclasses import fields
from pyexpat import model
# from socket import fromshare # Comment in Unix
from django import forms
from django.contrib.auth.models import User
from custom.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
