from django.db import models
import uuid


class TimeEntry(models.Model):
    time_spent = models.IntegerField(help_text="Unit is minutes.")
    entry_date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=600)
    job = models.ForeignKey('Job', to_field='uuid')


class Job(models.Model):
    uuid = models.CharField(max_length=64, unique=True, default=uuid.uuid1)
    title = models.CharField(max_length=120)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=6, decimal_places=4)
