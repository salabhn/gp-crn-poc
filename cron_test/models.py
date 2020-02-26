from django.db import models
import logging

logger = logging.getLogger('django')
# Create your models here.


class CronJob(models.Model):
    minute = models.CharField(max_length=8)
    hour = models.CharField(max_length=8)
    day_of_month = models.CharField(max_length=8)
    month = models.CharField(max_length=8)
    day_of_week = models.CharField(max_length=8)
    name = models.CharField(max_length=24)
    command = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "%s--%s" % (self.name, self.command)

    @property
    def schedule(self):
        return "%s %s %s %s %s" % (self.minute, self. hour, self.day_of_month, self.month, self.day_of_week)
