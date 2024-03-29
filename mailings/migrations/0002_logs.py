# Generated by Django 4.2.4 on 2024-02-17 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try', models.DateTimeField(verbose_name='дата и время последней попытки')),
                ('status_try', models.CharField(max_length=20, verbose_name='статус попытки')),
                ('server_answer', models.TextField(blank=True, default='', null=True, verbose_name='ответ сервера')),
                ('send_name', models.CharField(default=None, max_length=200, verbose_name='наименование рассылки')),
                ('send_email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='почта отправки')),
                ('logs_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
                'ordering': ('-last_try',),
            },
        ),
    ]
