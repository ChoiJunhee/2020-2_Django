from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm, RegisterForm

# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if(form.is_valid() and form.signed):
            return redirect('../login')
        else:
            return render(request, 'register.html', {'form':form})
    elif(request.method=='GET'):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})


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
    user_id = request.session.get('user')
    if(user_id):
        login_user = user.objects.get(pk=user_id)
    return HttpResponse(login_user.username)