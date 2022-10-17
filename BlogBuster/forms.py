from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from BlogBuster.models import *

class FormVHS(forms.ModelForm):
    class Meta:
        model = Vhs
        fields = ["titulo", "genero", "anioLanzamiento", "director", "imagen"]

class FormCds(forms.Form):
    nombre = forms.CharField()
    artista = forms.CharField()
    anioLanzamiento = forms.IntegerField()
    genero = forms.CharField()


class FormJuegos(forms.Form):
    nombre = forms.CharField()
    desarrolladora = forms.CharField()
    plataforma = forms.CharField()
    genero = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["email"]
        exclude = ["username"]
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]


