from django.conf.urls import patterns, include, url
from timetracking.views import HomeView, JobsView, JobsDetailView, JobsDeleteView, TimeEntriesView, TimeEntriesDetailView, TimeEntriesDeleteView, InvoiceView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^jobs/$', JobsView.as_view(), name='jobs'),
    url(r'^jobs/(?P<pk>\d+)/$', JobsDetailView.as_view(), name='jobs_details'),
    url(r'^jobs/(?P<pk>\d+)/invoice$', InvoiceView.as_view(), name='invoice'),
    url(r'^jobs/(?P<pk>\d+)/delete$', JobsDeleteView.as_view(), name='jobs_delete'),

    url(r'^time-entries/$', TimeEntriesView.as_view(), name='time_entries'),
    url(r'^time-entries/(?P<pk>\d+)/$', TimeEntriesDetailView.as_view(), name='time_entries_details'),
    url(r'^time-entries/(?P<pk>\d+)/delete$', TimeEntriesDeleteView.as_view(), name='time_entries_delete'),
)
