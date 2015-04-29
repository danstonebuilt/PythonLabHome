__author__ = 'daniel.anselmo'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
       url(r'^all/$', 'article.views.articles'),
       url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
       url(r'^1/(\d+)/$', 'article.views.show_tst'),
)