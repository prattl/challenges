import datetime


class Invoice():
    def __init__(self, job, start_date, end_date, time_entries):
        # Initialize some params and default values
        self.job = job
        self.start_date = start_date
        self.end_date = end_date
        self.time_entries = time_entries
        self.subtotal = 0
        self.tax = 0
        self.total = 0
