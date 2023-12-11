from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_name', 'placeholder': 'ваш логин:'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form_password', 'placeholder': 'ваш пароль:'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'is_employer')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_name', 'placeholder': 'имя:'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_last_name', 'placeholder': 'фамилия:'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form_email', 'placeholder': 'Email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_username', 'placeholder': 'ваш логин:'}))
    is_employer = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'form_checkbox'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form_password1', 'placeholder': 'ваш пароль:'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form_password2', 'placeholder': 'ваш пароль еще раз:'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_employer', 'password1', 'password2')
