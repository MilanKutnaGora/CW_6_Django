# Generated by Django 4.2.4 on 2024-02-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=30, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('contents', models.TextField(verbose_name='содержимое')),
                ('publication_date', models.DateField(verbose_name='дата публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
                'ordering': ('article_name',),
            },
        ),
    ]
