from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from googlemaps.waypoints.models import Waypoint
from django.contrib.gis.geos import Point
import simplejson

def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    return render_to_response('waypoints/index.html', {
        'waypoints': waypoints,
        'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    })

def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), mimetype='application/json')

def search(request):
    'Search/Rank waypoints'
    # Build searchPoint
    try:
        searchPoint = Point(float(request.GET.get('lng')), float(request.GET.get('lat')))
    except:
        return HttpResponse(simplejson.dumps(dict(isOk=0, message='Could not parse search point')))

    # Search database
    waypoints = Waypoint.objects.distance(searchPoint).order_by('distance')
    return HttpResponse(simplejson.dumps(dict(
                isOk=1,
                content=render_to_string('waypoints/waypoints.html', {
                        'waypoints': waypoints
                        }),
                waypointByID=dict((x.id, {
                            'name': x.name,
                            'lat' : x.geometry.y,
                            'lng' : x.geometry.x,
                            }) for x in waypoints),
                )), mimetype='application/json')

