# Generated by Django 3.0.5 on 2021-05-30 10:34

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, default='', max_length=30)),
                ('empleados', jsonfield.fields.JSONField(null=True)),
                ('creado', models.DateField(auto_now=True)),
                ('ts', models.DateField()),
                ('img', models.CharField(blank=True, default='', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('dni', models.CharField(blank=True, max_length=9)),
                ('registroTrabajo', jsonfield.fields.JSONField(blank=True, null=True)),
                ('settings', jsonfield.fields.JSONField(blank=True, null=True)),
                ('img', models.CharField(blank=True, default='', max_length=3000)),
                ('empresa', models.CharField(blank=True, default='', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
