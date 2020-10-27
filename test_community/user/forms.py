from django import forms
from .models import user
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import UserManager

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해 주세요.'
        },max_length=32, label='ID')
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해 주세요.'
        }, widget=forms.PasswordInput, max_length=32, label='Password')

    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if(username and password):
            if(not user.objects.filter(username__iexact=username)):
                self.add_error('username', '아이디가 존재하지 않습니다.')
            else:
                loginuser = user.objects.get(username=username)
                if(not (check_password(password, loginuser.password))):
                    self.add_error('password', '비밀번호가 일치하지 않습니다.')
                else:
                    self.user_id = loginuser.id
            


class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해 주세요.'
        },max_length=32, label='ID'
    )
    usermail = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해 주세요.'
        },max_length=64, label='usermail'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해 주세요.'
        }, widget=forms.PasswordInput, max_length=32, label='password'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호 확인을 입력해 주세요.'
        }, widget=forms.PasswordInput, max_length=32, label='re_password'
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        usermail = cleaned_data.get('usermail')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if(username and usermail and password and re_password):
            if(user.objects.filter(username__iexact=username)):
                self.add_error('username', '이미 존재하는 아이디 입니다.')
            elif(user.objects.filter(usermail__iexact=usermail)):
                self.add_error('usermail', '이미 존재하는 이메일 입니다.')
            elif(password != re_password):
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
            else:
                # USER 생성해야 하는 부분
                
                self.signed = True
        

