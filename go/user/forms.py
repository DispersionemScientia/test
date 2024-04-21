from django import forms
from django.core.validators import RegexValidator

from .models import User

class UserCreationForm(forms.ModelForm):
    email = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'username', 'email']
        labels = {'phone_number': 'Номер телефона', 'password': 'Пароль',
                  'username': 'Имя пользователя', 'email': 'Почта'}

class UserLoginForm(forms.Form):

    phone_number = forms.CharField(
        label='Введите номер телефона',
        max_length=15,
        validators=[RegexValidator(regex=r"^\+?1?\d{8,15}$")]
    )
    password = forms.CharField(label='Введите ваш пароль')