from django.urls import path
from django.views.generic import TemplateView
from .views import ProfileDetailVeiw, top_ten, statistics
#from routes.views import ResultListView, result

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('user/<int:pk>/',   ProfileDetailVeiw.as_view(template_name='home/profile.html'), name='profile'),
    path('topten/', top_ten, name='topten'),
    path('statistics/', statistics, name='statistics'),
]