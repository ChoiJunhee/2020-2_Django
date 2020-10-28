from django import forms
from .models import customUser as User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_field = ['password', 'chk_password']

        for field_name in class_update_field:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
    
    class Meta:
        model = User
        fields = (
            'userID',
            'userMail',
            'password'
            'chk_password',
            'profile_image',
            'UserType'
        )
        widgets = {
            'userID': forms.CharField(
                attrs={
                    'class': 'form-control',
                }
            ),
            'UserType': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }