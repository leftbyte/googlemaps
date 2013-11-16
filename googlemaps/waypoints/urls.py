# Import django modules
from django.conf.urls import *

urlpatterns = patterns('googlemaps.waypoints.views',
    url(r'^$', 'index', name='waypoints-index'),
    url(r'^save$', 'save', name='waypoints-save'),
)
