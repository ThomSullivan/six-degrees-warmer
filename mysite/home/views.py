import hashlib
import urllib
from mysite.settings import TMDB_API_KEY
import requests
from django import template
from django.shortcuts import render
from django.utils.safestring import mark_safe
from routes.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.models import User
from .models import Profile
from routes.models import Person, Step
from django.db.models import Count

register = template.Library()

class ProfileDetailVeiw(OwnerDetailView):
    model = User
    template_name = 'home/profile.html'
    def get(self, request, pk):

        user = User.objects.get(id=pk)
        fav_people_objects = [person for person in user.favorite_people.all()]
        fav_people_list = []
        for object in fav_people_objects:
            url = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(object.name, TMDB_API_KEY)
            details = requests.get(url, params=request.GET)
            instance = details.json()
            fav_people_list.append((instance['name'],object.id))
        profile = Profile.objects.get(user=user)
        ctx = {'user_profile':user,'profile':profile, 'favs':fav_people_list}
        return render(request, self.template_name, ctx)


def top_ten(self):
    q1 = Person.objects.annotate(fav_count=Count('favorites'))
    q1 = q1.order_by('-fav_count')[:10]
    ctx = {'person_list' : [] }
    counter = 1
    for object in q1:
            url = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(object.name, TMDB_API_KEY)
            details = requests.get(url)
            instance = details.json()
            ctx['person_list'].append((instance,object.id,counter))
            counter+=1
    return render(self, 'home/topten.html', ctx)

def statistics(self):
    total = Person.objects.count()
    info = Step.objects.values('next_step').annotate(c=Count('next_step')).order_by('-c').exclude(next_step=2469)[:10]
    ten_list = []
    for item in info:
        object = Person.objects.get(pk=item['next_step'])
        url = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(object.name, TMDB_API_KEY)
        details = requests.get(url)
        instance = details.json()
        ten_list.append((instance['name'],instance['profile_path'],object.id,item['c']))
    ctx = {'total':total, 'ten_list':ten_list}
    return render(self, 'home/statistics.html', ctx)

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
  default = "https://example.com/static/images/defaultavatar.jpg"
  return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(email.lower()).hexdigest(), urllib.urlencode({'d':default, 's':str(size)}))

# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" width="%d" height="%d">' % (url, size, size))