from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from xbmc.api.resources import TvShowResource, EpisodeResource, MovieResource

v1_api = Api(api_name='v1')
v1_api.register(TvShowResource())
v1_api.register(EpisodeResource())
v1_api.register(MovieResource())

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'media.views.home', name='home'),
    # url(r'^media/', include('media.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'webui.views.home', name='home'),
    
    (r'^api/', include(v1_api.urls)),
)
