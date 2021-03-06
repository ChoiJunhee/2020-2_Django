# Generated by Django 3.1.2 on 2020-10-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201023_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='customUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('age', models.CharField(choices=[('A', '~14'), ('B', '15~19'), ('C', '20~24'), ('D', '25~29'), ('E', '30~34'), ('F', '35~43'), ('G', '43~57'), ('H', '58~67'), ('I', '68~')], default='~14', max_length=10)),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_counseller', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('joind_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
