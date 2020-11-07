from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    form = UserCreationForm
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            messages.success(request, '계정이 생성되었습니다.')
            return redirect('signup')
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        return render(request, 'signup.html', {'form':form})


def login(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            request.session['user'] = form.user_id
            return redirect('/')
        else:
            return render(request, 'login.html', {'form':form})
    elif(request.method == 'GET'):
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

    
def home(request):
    return render(request, 'home.html')