from django.urls import path
from django.views.generic import TemplateView
from . import views
#from routes.views import ResultListView, result

app_name = 'routes'

urlpatterns = [
    path('', TemplateView.as_view(template_name='routes/index.html'), name='index'),
    path('<str:search>/', views.ResultDetailView.as_view(), name='result'),
    #path('routes/steps/', views.ResultListView.as_view()),
]