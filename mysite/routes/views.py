from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from mysite.settings import TMDB_API_KEY
# Create your views here.






def index(request):
    out_bound = 'https://api.themoviedb.org/3/person/4724?api_key={}'.format(TMDB_API_KEY)
    address = requests.get(out_bound, params=request.GET)
    ctx = json.loads(address.text)
    return render(request, 'routes/results.html', ctx)