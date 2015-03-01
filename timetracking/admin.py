from django.contrib import admin
from timetracking.models import TimeEntry, Job


class TimeEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('entry_date',)


admin.site.register(TimeEntry, TimeEntryAdmin)
admin.site.register(Job)
