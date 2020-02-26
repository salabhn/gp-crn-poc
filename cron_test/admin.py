from django.contrib import admin
from .models import CronJob
# Register your models here.


class CronJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'command', 'schedule', 'enabled')
    search_fields = ['name']

    fields = (
        'name',
        'command',
        ('minute', 'hour', 'day_of_month', 'month', 'day_of_week'),
        'enabled'
    )


admin.site.register(CronJob, CronJobAdmin)
