from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^timetracking/', include('timetracking.urls', namespace='timetracking')),
    url(r'^admin/', include(admin.site.urls)),
)
