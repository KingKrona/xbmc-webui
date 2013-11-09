from tastypie.resources import ModelResource
from tastypie import fields
from xbmc.models import TvShow, Episode, Movie


class TvShowResource(ModelResource):
    class Meta:
        queryset = TvShow.objects.all()
        allowed_methods = ['get']
        
class EpisodeResource(ModelResource):
    class Meta:
        queryset = Episode.objects.all()
        allowed_methods = ['get']

    show = fields.ForeignKey(TvShowResource, 'show')
    
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        allowed_methods = ['get']
        
