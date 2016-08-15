from django.test import TestCase
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.views.generic import ListView

from vigilante import views

# Create your tests here.

router = DefaultRouter()
# router.register(r'snippets', views.SnippetView)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^index/$', views.index, name='index'),
    url(r'^results/', views.placeresults, name='results')


)