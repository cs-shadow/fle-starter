from django.shortcuts import render
import urllib2
import json

def landing_page(request):
    raw_data = urllib2.urlopen("http://127.0.0.1:8000/static/data/movies.json").read()
    data = json.loads(raw_data)
    movies = data['movies']
    return render(request, "starter/landing_page.html", {"movies": movies})
