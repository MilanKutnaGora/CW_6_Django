# Generated by Django 4.2.4 on 2024-02-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, default='41213226', max_length=8, null=True, verbose_name='код подтверждения почты'),
        ),
    ]
