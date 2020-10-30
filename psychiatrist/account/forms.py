from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from .models import User, UserManager

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label=_('EMAIL'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':_('Email address'),
                'required':'True',
            }
        )
    )

    nickname = forms.CharField(
        label = _('Nickname'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':_('Nickname'),
                'required':'True',
            }
        )
    )

    USER_AGE_CHOICE = (
        ('A', '~14'),
        ('B', '15~19'),
        ('C', '20~24'),
        ('D', '25~29'),
        ('E', '30~34'),
        ('F', '35~43'),
        ('G', '43~57'),
        ('H', '58~67'),
        ('I', '68~'),
    )

    ## ages 왜 안뜨지?
    ages = forms.ChoiceField(
        choices = USER_AGE_CHOICE, label="Ages", initial='', 
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': _('Ages'),
                'required': 'True',
            }
        ), required=True
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'nickname', 'ages')
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.clean_data.get('password2')
        if(password1 and password2):
            if(password1 != password2):
                raise forms.ValidationError('passwords do not match')
            return password1
        else:
            raise forms.ValidationError('enter your password')
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password1 = ReadOnlyPasswordHashField(
        label=_('password')
    )
    ages = forms.CharField(
        label = _('ages'),
        required=True,
    )

    class Meta:
        model = User
        fields=('email', 'password', 'ages', 'is_active', 'is_superuser')
    
    def clean_password(self):
        return self.initial['password']
        