from django.db import models

# Create your models here.
class Movie(models.Model):
    class Meta:
        managed = False
        db_table = 'movie'
        ordering = ['-id']
        
    id = models.IntegerField(primary_key=True,db_column='idMovie')
    file = models.ForeignKey('File', db_column='idFile')
    
    title = models.TextField(db_column='c00')
    plot_summary = models.TextField(db_column='c01')
    plot_outline = models.TextField(db_column='c02')
    tagline = models.TextField(db_column='c03')
    votes = models.TextField(db_column='c04')
    rating = models.TextField(db_column='c05')
    writers = models.TextField(db_column='c06')
    year_released = models.TextField(db_column='c07')
    thumbnails = models.TextField(db_column='c08')
    imdb_id = models.TextField(db_column='c09')
    sort_title = models.TextField(db_column='c10')
    runtime = models.TextField(db_column='c11')
    content_rating = models.TextField(db_column='c12')
    imdb_ranking = models.TextField(db_column='c13')
    genre = models.TextField(db_column='c14')
    director = models.TextField(db_column='c15')
    original_title = models.TextField(db_column='c16')
    studio = models.TextField(db_column='c18')
    trailer_url = models.TextField(db_column='c19')
    fanart_urls = models.TextField(db_column='c20')
    country = models.TextField(db_column='c21')
    path = models.TextField(db_column='c23')

class TvShow(models.Model):
    class Meta:
        managed = False
        db_table = 'tvshow'
        ordering = ['title']
        
    id = models.IntegerField(primary_key=True,db_column='idShow')
    
    title = models.TextField(db_column='c00')
    plot_summary = models.TextField(db_column='c01')
    status = models.TextField(db_column='c02')
    votes = models.TextField(db_column='c03')
    rating = models.TextField(db_column='c04')
    first_aired = models.TextField(db_column='c05')
    thumbnail_url = models.TextField(db_column='c06')
    genre = models.TextField(db_column='c08')
    original_title = models.TextField(db_column='c09')
    episode_guide_url = models.TextField(db_column='c10')
    fan_art_url = models.TextField(db_column='c11')
    series_id = models.TextField(db_column='c12')
    content_rating = models.TextField(db_column='c13')
    network = models.TextField(db_column='c14')
    sort_title = models.TextField(db_column='c15')
    path = models.TextField(db_column='c16')
    
    
class Episode(models.Model):
    class Meta:
        managed = False
        db_table = 'episode'
        ordering = ['-id']
        
    id = models.IntegerField(primary_key=True, db_column='idEpisode')
    file = models.ForeignKey('File', db_column='idFile')
    show = models.ForeignKey('TvShow', db_column='idShow')
    
    title = models.TextField(db_column='c00')
    plot_summary = models.TextField(db_column='c01')
    votes = models.TextField(db_column='c02')
    rating = models.TextField(db_column='c03')
    writer = models.TextField(db_column='c04')
    first_aired = models.TextField(db_column='c05')
    thumbnail_url = models.TextField(db_column='c06')
    watched = models.TextField(db_column='c08')
    length = models.TextField(db_column='c09')
    director = models.TextField(db_column='c10')
    season = models.TextField(db_column='c12')
    episode = models.TextField(db_column='c13')
    original_title = models.TextField(db_column='c14')
    sort_season = models.TextField(db_column='c15')
    sort_episode = models.TextField(db_column='c16')
    bookmark = models.TextField(db_column='c17')
    path = models.TextField(db_column='c18')
    
class File(models.Model):
    class Meta:
        managed = False
        db_table = 'files'
        ordering = ['-id']
        
    id = models.IntegerField(primary_key=True, db_column='idFile')
    path = models.ForeignKey('Path', db_column='idPath')
    
    filename = models.TextField(db_column='strFilename')
    play_count = models.IntegerField(db_column='playCount')
    last_played = models.TextField(db_column='lastPlayed')
    date_added = models.TextField(db_column='dateAdded')
    
class Path(models.Model):
    class Meta:
        managed = False
        db_table = 'path'
        ordering = ['-id']
        
    id = models.IntegerField(primary_key=True, db_column='idPath')
    
    path = models.TextField(db_column='strPath')
    content = models.TextField(db_column='strContent')
    scraper = models.TextField(db_column='strScraper')
    hash = models.TextField(db_column='strHash')
    scan_recursive = models.IntegerField(db_column='scanRecursive')
    use_folder_names = models.BooleanField(db_column='useFolderNames')
    settings = models.TextField(db_column='strSettings')
    no_update = models.BooleanField(db_column='noUpdate')
    exclude = models.BooleanField(db_column='exclude')
    date_added = models.TextField(db_column='dateAdded')