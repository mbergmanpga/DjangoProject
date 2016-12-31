''' This is the default mapping from the django project to the rango app so that ^rango/ requests can be parsed '''

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

