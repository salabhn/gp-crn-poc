from django.db.models.signals import post_save
from django.dispatch import receiver
from kubernetes import client, config
from openshift.dynamic import DynamicClient
import logging

from .models import CronJob

logger = logging.getLogger('django')


@receiver(post_save, sender=CronJob)
def update_cron_job(sender, instance, created, **kwargs):
    logger.info('LOG WORKING')
    config.load_incluster_config()
    logger.info(client.Configuration)
    logger.info(dir(client.Configuration()))
    v1 = client.ApiClient()
    dyn_client = DynamicClient(v1)
    v1_services = dyn_client.resources.get(api_version='v1', kind='Pod')
    logger.info('PODS::: %s' % dir(v1_services))
    pods = v1_services.get()
    for pod in pods:
        logger.info('POD:::%s' % pod)
        logger.info(dir(pod))

    v1_services = dyn_client.resources.get(api_version='v1', kind='CronJob')
    logger.info('CronJobs::: %s' % dir(v1_services))
    pods = v1_services.get()
    for pod in pods:
        logger.info('CronJob:::%s' % pod)
        logger.info(dir(pod))
