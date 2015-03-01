from django.conf.urls import patterns, include, url
from django.contrib import admin
from timetracking.views import HomeView, JobsView, TimeEntriesView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^jobs/$', JobsView.as_view(), name='jobs'),
    url(r'^time-entries/$', TimeEntriesView.as_view(), name='time_entries'),
    url(r'^admin/', include(admin.site.urls)),
)
