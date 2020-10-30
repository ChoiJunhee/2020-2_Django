from django import forms
from .models import customUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password, make_password

