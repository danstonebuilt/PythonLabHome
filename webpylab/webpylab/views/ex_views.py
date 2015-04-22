# -*- coding: utf-8 -*-
__author__ = 'daniel.anselmo'
import os

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello_user(request):
    name = 'Daniel Stonebuilt'
    html = '<html><body>Hi %s, this seems to have worked</body></html>' % name
    return HttpResponse(html)

def hello_user_tplt(request):
    c = get_template('hello.html')
    html = c.render(Context({'user_name': __author__}))
    return HttpResponse(html)


def show_prj_dir(request):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    tmp_dir = os.path.join(base_dir, 'templates').replace('\\', '/')
    return HttpResponse(tmp_dir)