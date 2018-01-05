"""
Definition of models.
"""

from django.db import models

# Create your models here.
class MusicGenre(models.Model):
    genrename = models.CharField(max_length=50)
    isactive = models.BooleanField(default=True)    
    def __str__(self):
        return '%d %s' % (self.id, self.genrename)

class MusicAlbum(models.Model):
    genre = models.ForeignKey(MusicGenre,on_delete=models.CASCADE)
    albumname = models.CharField(max_length=100)
    relase_date = models.DateField()
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return '%d %s' % (self.id, self.albumname)

class MusicSong(models.Model):
    musicalbum = models.ForeignKey(MusicAlbum,on_delete=models.CASCADE)
    songname = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return '%d %s' % (self.id, self.songname)
