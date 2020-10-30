from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import uuid

class customUserManager(BaseUserManager):
    def create_user(self, email, nickname, age, password, **extra_fields):
        try:
            user = self.model(
                nickname = nickname,
                email = email,
                age = age
            )
            extra_fields.setdefault('is_active', True)
            extra_fields.setdefault('is_counseller', False)
            extra_fields.setdefault('is_manager', False)
            extra_fields.setdefault('is_superuser', False)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)
    
    def create_superuser(self, email, nickname, password, **extra_fields):
        try:
            superuser = self.create_user(
                user_type = customUser.USER_TYPES[3],
                email = email,
                nickname = nickname,
                password = password,
            )
            superuser.is_admin = True
            superuser.is_superuser = True
            superuser.is_manager = True
            superuser.is_counseller = True
            superuser.is_active = True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)



class customUser(AbstractBaseUser):
    # Default field : id, password, last_login

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

    

    email = models.EmailField(max_length=64, null=False, unique=True)
    nickname = models.CharField(max_length=16, unique=True)
    age = models.CharField(
        max_length=10,
        choices = USER_AGE_CHOICE,
        default = USER_AGE_CHOICE[0][1]
    )

    is_active = models.BooleanField(default=True)
    is_counseller = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    joind_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = customUserManager()