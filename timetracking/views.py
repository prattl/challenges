from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from timetracking.models import Job, TimeEntry


class HomeView(TemplateView):
    template_name = 'timetracking/index.html'


class JobsView(View):
    template = 'timetracking/jobs.html'


    def dispatch(self, request, *args, **kwargs):
        self.tvars = {}
        return super(JobsView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        # Render this template with a list of all jobs
        jobs = Job.objects.all()
        self.tvars['jobs'] = jobs

        return render(request, self.template, self.tvars)



class TimeEntriesView(View):
    template = 'timetracking/timeentries.html'


    def dispatch(self, request, *args, **kwargs):
        self.tvars = {}
        return super(TimeEntriesView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.tvars)
