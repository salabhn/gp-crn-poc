from django.core.management import BaseCommand
import logging

logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("CRON SCHEDULE WAS A SUCCESS!!!")
