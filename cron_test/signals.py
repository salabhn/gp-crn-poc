from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

from .models import CronJob


logger = logging.getLogger('django')

@receiver(post_save, sender=CronJob)
def update_chargebee_add_on(sender, instance, created, **kwargs):
    logger.info('LOG WORKING')