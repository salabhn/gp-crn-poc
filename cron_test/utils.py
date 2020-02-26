from kubernetes import client, config

from .models import CronJob


def sync_cron_jobs():
    config.load_incluster_config()
    kube_cron_job_client = client.BatchV1beta1Api()
    cron_jobs = kube_cron_job_client.list_namespaced_cron_job('cron-poc')
    new_jobs = []
    for cron_job in cron_jobs['items']:
        name = cron_job['metadata']['name']
        if not CronJob.objects.filter(name=name).exists():
            command = " ".join(cron_job['spec']['job_template']['spec']['template']['spec']['containers'][0]['command'])
            schedule = cron_job['spec']['schedule']
            enabled = not cron_job['spec']['suspend']
            minute, hour, day_of_month, month, day_of_week = schedule.split(' ')
            job = {
                'name': name,
                'command': command,
                'enabled': enabled,
                'minute': minute,
                'hour': hour,
                'day_of_month': day_of_month,
                'day_of_week': day_of_week
            }
            new_jobs.append(CronJob(**job))
