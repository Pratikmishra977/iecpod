from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'RePassword'}))


    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password', 'repassword']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}),
        }

# class SignupForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
#

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}),
        }