from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _ 

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, ages, password=None):
        if not email:
            raise ValueError(_('이메일을 입력해 주세요.'))
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            ages = ages,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, ages, password=None):
        user = self.create_user(
            email = email,
            nickname=nickname,
            ages=ages,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = _('Email Address'),
        max_length = 64,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name = _('nickname'),
        max_length = 16,
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

    ages = models.CharField(
        max_length=10,
        choices = USER_AGE_CHOICE,
        default = USER_AGE_CHOICE[0][1]
    )
    is_active = models.BooleanField(
        verbose_name=_('ACTIVE'),
        default = True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('STAFF'),
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Joined'),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'ages', ]

    class Meta:
        verbose_name=_('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

        def __str__(self):
            return self.nickname

        


# Create your models here.
