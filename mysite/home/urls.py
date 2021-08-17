from django.urls import path
from django.views.generic import TemplateView
from . import views
#from routes.views import ResultListView, result

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]