from timetracking.models import Job, TimeEntry
from timetracking.invoice import Invoice
from datetime import date
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # Pull some test date
        job = Job.objects.all()[0]
        date1 = date(2015, 3, 2)
        date2 = date(2015, 3, 3)

        job.invoice(date1, date2)
