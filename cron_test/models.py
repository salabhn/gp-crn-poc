from django.db import models
import logging

logger = logging.getLogger('django')
# Create your models here.
logger.info("It's working!")


class CronJob(models.Model):
    minute = models.CharField(max_length=8)
    hour = models.CharField(max_length=8)
    day_of_month = models.CharField(max_length=8)
    month = models.CharField(max_length=8)
    day_of_week = models.CharField(max_length=8)
