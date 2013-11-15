from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

def index(request):
    'Display map'
    return render_to_response('waypoints/index.html', {
    })
