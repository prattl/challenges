import datetime


class Invoice():
    """
    This class just defines some variables relavant to an invoice. It also
    calculates the totals based on the hob and time entries. To improve the
    class, we should make it JSON-serializable (as opposed to just returning a
    dict of strings in the to_json() method). We should also verify that we
    have a valid job and time entries assigned with some exception handling,
    in the even that there is some data missing.
    """
    def __init__(self, job, start_date, end_date, time_entries):
        # Initialize some params and default values
        self.job = job
        self.start_date = start_date
        self.end_date = end_date
        self.time_entries = time_entries
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.calculate_totals()


    def calculate_totals(self):
        hourly_rate = self.job.hourly_rate
        tax_rate = self.job.tax_rate / 100
        total_minutes = sum([time_entry.time_spent for time_entry in self.time_entries])

        self.subtotal = hourly_rate * total_minutes / 60
        self.tax = self.subtotal * tax_rate
        self.total = self.subtotal + self.tax


    def to_json(self):
        # Return a dict of JSON-serializable data
        # TODO: Make this object itself serializable
        # This would require making the TimeEntry and Job classes serializable as well.
        return {
                'job': unicode(self.job),
                'start_date': unicode(self.start_date),
                'end_date': unicode(self.end_date),
                'time_entries': [unicode(entry) for entry in self.time_entries],
                'subtotal': self.subtotal,
                'tax': self.tax,
                'total': self.total,
        }

