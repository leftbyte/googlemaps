from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# Import custom modules
from googlemaps.waypoints.models import Waypoint

# Create your views here.
from django.http import HttpResponse

def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    return render_to_response('waypoints/index.html', {
        'waypoints': waypoints,
        'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    })
