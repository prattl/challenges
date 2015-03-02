from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from timetracking.models import Job, TimeEntry

import datetime


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
    """
    Implement the Jobs view as a CreateView so we can create new records easily 
    on the main Jobs page. Also for all of these views, we are using the
    object's pk as an identifier because that is just the default behavior.
    We could override this with the get_object() method, and use an alternative
    identifier (like a slug or uuid) instead.

    Improvements:
    Render the page initially without the jobs and load those via ajax
    """

    template_name = 'timetracking/jobs/jobs.html'
    model = Job


    def get_context_data(self, *args, **kwargs):
        # We want to display a list of all jobs on this page, so add them to
        # the context.
        context = super(JobsView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


class JobsDetailView(AjaxableResponseMixin, UpdateView):
    template_name = 'timetracking/jobs/jobs_detail.html'
    model = Job


class JobsDeleteView(AjaxableResponseMixin, DeleteView):
    template_name = 'timetracking/jobs/jobs_delete.html'
    model = Job
    success_url = reverse_lazy('timetracking:jobs')


class TimeEntriesView(AjaxableResponseMixin, CreateView):
    template_name = 'timetracking/time_entries/time_entries.html'
    model = TimeEntry

    def get_context_data(self, *args, **kwargs):
        # We want to display a list of all time entries on this page, so add them to
        # the context.
        context = super(TimeEntriesView, self).get_context_data(**kwargs)
        context['time_entries'] = TimeEntry.objects.all()
        return context


class TimeEntriesDetailView(AjaxableResponseMixin, UpdateView):
    template_name = 'timetracking/time_entries/time_entries_detail.html'
    model = TimeEntry


class TimeEntriesDeleteView(AjaxableResponseMixin, DeleteView):
    template_name = 'timetracking/time_entries/time_entries_delete.html'
    model = TimeEntry
    success_url = reverse_lazy('timetracking:time_entries')


class InvoiceView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            # Retrieve the job we are looking at
            job_pk = kwargs.pop('pk')
            try:
                job = Job.objects.get(pk=job_pk)
            except Job.DoesNotExist as e:
                return JsonResponse({'errors': str(e)}, status=400)

            # Validate the date ranges
            # TODO: This should all be done in a Django Form
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            date_errors = None
            try:
                date1 = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            except Exception as e:
                date_errors = {'errors': 'Date is not correct format'}

            if date1 > date2:
                date_errors = {'errors': 'Date 1 must be less than date 2'}

            if date_errors:
                return JsonResponse(date_errors, status=400)

            # Generate and send back the invoice
            invoice = job.invoice(date1, date2)
            return JsonResponse(invoice.to_json())

        else:
            return JsonResponse({'errors': 'Request is not ajax.'}, status=400)


