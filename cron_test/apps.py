from django.apps import AppConfig


class CronTestConfig(AppConfig):
    name = 'cron_test'

    def ready(self):
        from . import signals