from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'data-required':'true', 'placeholder':'Username', 'class':'form-control',}),
        label=("Username"))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'data-required':'true', 'placeholder':'Password','class':'form-control',}),
        label=("Password"))