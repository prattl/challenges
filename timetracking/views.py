from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from timetracking.models import Job, TimeEntry


class HomeView(TemplateView):
    template_name = 'timetracking/index.html'


class AjaxableResponseMixin(object):
    """
    From Django documentation: 
    https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-editing/
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            if type(self.object) is Job:
                data = serializers.serialize('json', [self.object])[1:-1]
            else:
                data = {
                    'pk': self.object.pk,
                }
            return JsonResponse(data, safe=False)
        else:
            return response



class JobsView(AjaxableResponseMixin, CreateView):
    # Implement the Jobs view as a CreateView so we can create new records easily 
    # on the main Jobs page.
    template_name = 'timetracking/jobs/jobs.html'
    model = Job


    def get_context_data(self, *args, **kwargs):
        context = super(JobsView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


    def dispatch(self, request, *args, **kwargs):
        self.tvars = {}
        return super(JobsView, self).dispatch(request, *args, **kwargs)


    # def get(self, request, *args, **kwargs):
        # Render this template with a list of all jobs
        # jobs = Job.objects.all()
        # self.tvars['jobs'] = jobs
        # return render(request, self.template_name, self.tvars)


class JobsDetailView(AjaxableResponseMixin, UpdateView):
    template_name = 'timetracking/jobs/jobs_detail.html'
    model = Job


    def dispatch(self, request, *args, **kwargs):
        return super(JobsDetailView, self).dispatch(request, *args, **kwargs)


class TimeEntriesView(View):
    template = 'timetracking/timeentries.html'


    def dispatch(self, request, *args, **kwargs):
        self.tvars = {}
        return super(TimeEntriesView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.tvars)
