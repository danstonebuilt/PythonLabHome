from django.conf.urls import patterns, url

__author__ = 'Daniel'


urlpatterns = patterns('',
    url(r'^base$', 'lab.views.showbase'),
)