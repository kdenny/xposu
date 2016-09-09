from django.conf.urls import patterns, include, url
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
from vigilante.models import Store
from vigilante import views

urlpatterns = patterns('',
    # Examples:

    url(r'^$', views.index, name='index'),
    url(r'^vigilante/', include('vigilante.urls')),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Store), name='data'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
