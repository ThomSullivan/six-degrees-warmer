from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
import requests
from mysite.settings import TMDB_API_KEY
from .models import Step, Person, Movie
# Create your views here.
from django.views.generic import DetailView


class ResultDetailView(DetailView):
    model = Person
    template_name = 'routes/results.html'
    def get(self, request, search):
        ctx = {'degrees':[]}
        bacon = False
        search = 'https://api.themoviedb.org/3/search/person?api_key={}&query={}'.format(TMDB_API_KEY, request.GET['search'])
        address = requests.get(search, params=request.GET)
        object = address.json()
        person_id = object['results'][0]['id']
        counter = 0
        while bacon == False:
            try:
                x = Person.objects.get(name=person_id)
            except:
                x = Person.objects.filter(name=person_id)[0]
            y = Step.objects.get(person=x)
            details = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(y.person.name, TMDB_API_KEY)
            details = requests.get(details, params=request.GET)
            instance1 = details.json()
            details = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(y.movie.title, TMDB_API_KEY)
            details = requests.get(details, params=request.GET)
            instance = details.json()

            ctx['degrees'].append((instance1['name'],instance1['profile_path'],instance['title'],instance['poster_path']))
            person_id = y.next_step.name
            counter += 1
            if person_id == 4724:
                bacon = True



        return render(request, self.template_name, ctx)




def result(request, search):

    search = 'https://api.themoviedb.org/3/search/person?api_key={}&query={}'.format(TMDB_API_KEY, request.GET['search'])
    address = requests.get(search, params=request.GET)
    object = address.json()
    person_id = object['results'][0]['id']
    details = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(person_id, TMDB_API_KEY)
    details = requests.get(details, params=request.GET)
    ctx = details.json()
    return render(request, 'routes/results.html', ctx)