# -*- coding: utf-8 -*-
__author__ = 'daniel.anselmo'
import os

from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'home.html')

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

def hello_template_simple(request):
    name = __author__
    return render_to_response('hello.html', {'user_name': name})

class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['user_name'] = __author__
        return context