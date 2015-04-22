from django.conf.urls import patterns, include, url
from django.contrib import admin
from webpylab.views.ex_views import hello_user, show_prj_dir

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webpylab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', hello_user),
    url(r'^dir/', show_prj_dir),
    url(r'^admin/', include(admin.site.urls)),
)
