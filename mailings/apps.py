from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

class DjangoApschedulerConfig(AppConfig):
    name = "django_apscheduler"
    verbose_name = "Django APScheduler"