__author__ = 'Daniel'

from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def current_datetime(request):
   now = datetime.datetime.now()
   return render_to_response('current_datetime.html', {'current_date': now})
