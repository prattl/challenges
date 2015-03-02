from django.db import models
from django.core import serializers
from django.core.urlresolvers import reverse
from timetracking.invoice import Invoice
import uuid


class TimeEntry(models.Model):
    time_spent = models.IntegerField(help_text="Unit is minutes.")
    entry_date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=600)
    job = models.ForeignKey('Job', to_field='uuid')


    def get_absolute_url(self):
        return reverse('timetracking:time_entries_details', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Time Entry'
        verbose_name_plural = 'Time Entries'


    def __unicode__(self):
        return u"Time entry for {} on {}, {} minutes".format(self.job, self.entry_date, self.time_spent)


    def __repr__(self):
        return "<TimeEntry: {}>".format(unicode(self))


class Job(models.Model):
    uuid = models.CharField(max_length=64, unique=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=120)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=6, decimal_places=4)


    def invoice(self, start_date, end_date):
        # Find time entries within the date range
        time_entries = TimeEntry.objects.filter(entry_date__range=(start_date, end_date))

        # Create an Invoice object
        new_invoice = Invoice(job=self, start_date=start_date, end_date=end_date, time_entries=time_entries)
        return new_invoice


    def get_absolute_url(self):
        return reverse('timetracking:jobs_details', kwargs={'pk': self.pk})


    def __unicode__(self):
        return unicode(self.title)


    def __repr__(self):
        return '<Job: {} - {}>'.format(self.title, self.uuid)


