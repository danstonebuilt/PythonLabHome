# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Megasena

# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = Q(dayOfWeak_icontains=query)
        result = Megasena.objects.filter(qset)
    else:
        result = []
        return render_to_response("lotery/megasena.html")


