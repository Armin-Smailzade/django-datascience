from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserCreateForm(UserCreationForm):
	
	email = forms.EmailField(required=True, label="Email", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name':'email'}))

	username = forms.CharField(required=True, label="Username", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name':'username'}))
	password1 = forms.CharField(required=True, label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'name':'password1'}))
	password2 = forms.CharField(required=True, label="Password Confirmation", max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'name':'password2'}))

	class Meta:
	    model = User
	    fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
	    user = super(UserCreateForm, self).save(commit=False)
	    user.email = self.cleaned_data["email"]
	    if commit:
	        user.save()
	    return user