### Django Project

---

This project aims to build a personal homepage using AWS and Django.



##### Procedure

---

1. [AWS Getting Started](https://aws.amazon.com/ko/getting-started/hands-on/websites/) > Python Web Application
   * using a Amazon Lightsail (Virtual Server, Storage, Database, Networking, etc.)

2. Create a Lightsail Instance.

   * 5$/Month... (1vCPU, 1GB RAM, 40GB SSD)

3. Django Project Start

   > cd /opt/bitnami/apps/django/django_projects && \ django-admin.py startproject testproject

   > cd testproject && python3 manage.py hello

4. Add a Django Application Code

   > sudo vim /opt/bitnami/apps/django/django_projects/testproject/hello/views.py
   >
   > > from django.http import HttpResponse
   > >
   > > def index(request):
   > >
   > > ​    return HttpResponse("Hello")

   > sudo vim /opt/bitnami/apps/django/django_projects/testprojects/hello/urls.py
   >
   > > from django.urls import path
   > >
   > > from . import views
   > >
   > > urlpatterns = [
   > >
   > > ​    path('', views.index, name='index'),]

   > sudo vim /opt/bitnami/apps/django/testproject/hello/urls.py
   >
   > > from django.contrib import admin
   > >
   > > from django.urls import include, path
   > >
   > > urlpatterns = [
   > >
   > > ​    path('', include('hello.urls')),
   > >
   > > ​    path('admin/', admin.site.urls),]

5. Test a Django Application

6. Application Hosting used a Apache