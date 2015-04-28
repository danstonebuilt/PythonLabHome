from django.conf.urls import patterns, include, url
from django.contrib import admin

from webpylab.views.ex_views import hello_user, show_prj_dir, hello_user_tplt
from webpylab.views.ex_views import HelloTemplate


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webpylab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'webpylab.views.ex_views.home'),
    # url(r'^hello/', hello_user),
    #url(r'^dir/', show_prj_dir),
    #url(r'^tmp/', hello_user_tplt),
    #url(r'^class_view/', HelloTemplate.as_view()),
    (r'^article/', include('article.url')),
    (r'^tst/', include('article.url')),
    url(r'^admin/', include(admin.site.urls)),
)
