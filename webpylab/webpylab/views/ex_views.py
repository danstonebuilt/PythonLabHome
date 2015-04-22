__author__ = 'daniel.anselmo'
import os
from django.http import HttpResponse

def hello_user(request):
    name = 'Daniel Stonebuilt'
    html = '<html><body>Hi %s, this seems to have worked</body></html>' % name
    return HttpResponse(html)

def show_prj_dir(request):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    tmp_dir = os.path.join(base_dir, 'templates')
    return HttpResponse(tmp_dir)