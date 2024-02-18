# Generated by Django 4.2.4 on 2024-02-17 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.CharField(max_length=150, unique=True, verbose_name='контактный email')),
                ('client_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('client_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('client_name',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='тема письма')),
                ('text', models.TextField(verbose_name='текст письма')),
                ('message_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='SendOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_name', models.CharField(default=None, max_length=200, verbose_name='наименование рассылки')),
                ('send_start', models.DateTimeField(default=None, verbose_name='время начала рассылки')),
                ('send_finish', models.DateTimeField(default=None, verbose_name='время окончания рассылки')),
                ('next_try', models.DateTimeField(blank=True, null=True, verbose_name='следующая попытка')),
                ('send_period', models.CharField(choices=[('Ежедневно', 'Ежедневно'), ('Еженедельно', 'Еженедельно'), ('Ежемесячно', 'Ежемесячно')], default='', max_length=20, verbose_name='периодичность')),
                ('send_status', models.CharField(choices=[('Создана', 'Создана'), ('Запущена', 'Запущена'), ('Завершена', 'Завершена')], default='Создана', max_length=20, verbose_name='статус рассылки')),
                ('is_active', models.BooleanField(default=True, verbose_name='активность')),
                ('client_email', models.ManyToManyField(to='mailings.client', verbose_name='контактный email')),
                ('mail_title', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='тема рассылки')),
                ('options_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
                'ordering': ('send_start',),
            },
        ),
    ]
