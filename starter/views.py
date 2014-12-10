from django.shortcuts import render
import urllib2
import json

def landing_page(request):
    raw_data = urllib2.urlopen("http://127.0.0.1:8000/static/data/movies.json").read()
    data = json.loads(raw_data)
    all_movies = data['movies']
    movies = []
    search_query = request.GET['search'] if 'search' in request.GET else ""
    # Filter movies containing the search string.
    for movie in all_movies:
        if search_query.lower() in movie['title'].lower():
            movies.append(movie)
    return render(request, "starter/landing_page.html", {"movies": movies})
