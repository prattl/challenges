from timetracking.models import Job, TimeEntry
from timetracking.invoice import Invoice
from datetime import date
from django.core.management.base import NoArgsCommand
from django.core import serializers


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # Pull some test date
        job = Job.objects.all()[0]
        date1 = date(2015, 3, 2)
        date2 = date(2015, 3, 3)

        invoice = job.invoice(date1, date2)
        print 'Got invoice: '
        print invoice

        json_data = serializers.serialize('json', Job.objects.filter(id=job.id))
        print 'JSON data: '
        print json_data
        

        # json = invoice.to_json()
        # print 'Got json: '
        # print json
        # print 'Type: %s' % type(json)
