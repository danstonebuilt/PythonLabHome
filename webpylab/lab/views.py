from django.shortcuts import render_to_response


# Create your views here.
def showbase(request):
    return render_to_response('new_home.html')