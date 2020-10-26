from django import forms
from .models import user
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label='ID')
    password = forms.CharField(widget=forms.PasswordInput, max_length=32, label='Password')

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if(username and password):
            loginuser = user.objects.get(username=username)
            if(not (check_password(password, loginuser.password))):
                self.add_error('password', 'wrong password')
