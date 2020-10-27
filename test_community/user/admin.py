from django.contrib import admin
from .models import user

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display =('id','username', 'usermail', 'password')

admin.site.register(user, userAdmin)