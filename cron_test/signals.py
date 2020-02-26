from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import yaml
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.template import Context
from kubernetes import client, config
import logging

from .models import CronJob

logger = logging.getLogger('django')


@receiver(post_save, sender=CronJob)
def update_cron_job(sender, instance, created, **kwargs):
    context = Context({
        'schedule': instance.schedule,
        'command': mark_safe(instance.command.split(' ')),
        'disabled': not instance.enabled,
        'name': instance.name
    })
    cron_definition = yaml.load(render_to_string('cron_test/sample.yml', context))

    # Load the default configuration of the cluster
    config.load_incluster_config()
    kube_cron_job_client = client.BatchV1beta1Api()
    cron_job = client.V1beta1CronJob()
    for key, value in cron_definition.items():
        setattr(cron_job, key, value)
    if created:
        try:
            kube_cron_job_client.create_namespaced_cron_job('cron-poc', cron_job)
        except Exception as e:
            logger.info("Error creating cron job:%s" % e)
    else:
        try:
            kube_cron_job_client.replace_namespaced_cron_job(instance.name, 'cron-poc', cron_job)
        except Exception as e:
            logger.info("Error updating cron job: %s" % e)


@receiver(post_delete, sender=CronJob)
def delete_cron_job(sender, instance, **kwargs):
    # Load the default configuration of the cluster
    config.load_incluster_config()
    kube_cron_job_client = client.BatchV1beta1Api()
    kube_cron_job_client.delete_namespaced_cron_job(instance.name, 'cron-poc')
