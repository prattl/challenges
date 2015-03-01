from django.contrib import admin
from timetracking.models import TimeEntry, Job


class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


class TimeEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('entry_date',)


admin.site.register(TimeEntry, TimeEntryAdmin)
admin.site.register(Job, JobAdmin)
