"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def genres(request):
    try:
        allGenres = MusicGenre.objects.all()
    except MusicGenre.DoesNotExist:
        raise Http404('Music Genres Does Not Exist')
    return render(request,"genre/index.html",{'genres':allGenres})

def searchGenres(request,genrename):
    try:
        allGenres = MusicGenre.objects.filter(genrename)
    except MusicGenre.DoesNotExist:
        raise Http404('Music Genres Does Not Exist')
    return render(request,"genre/index.html",{'genres':allGenres})

def genresDetail(request,genre_id):
    try:
        genresDetail = MusicGenre.objects.get(pk=genre_id)
    except MusicGenre.DoesNotExist:
        raise Http404('Music Genres Does Not Exist')
    return render(request,"genre/detail.html",{'genredetail':genresDetail})

def albums(request):
    try:
        allAlbums = MusicAlbum.objects.all()
    except MusicAlbum.DoesNotExist:
        raise Http404('Music Album Does Not Exist')
    return render(request,"album/index.html",{'albums':allAlbums})

def searchAlbums(request,genrename):
    try:
        allAlbums = MusicAlbum.objects.filter(genre=genrename)
    except MusicAlbum.DoesNotExist:
        raise Http404('Music Album Does Not Exist')
    return render(request,"album/index.html",{'albums':allAlbums})

def albumDetail(request,album_id):
    try:
        albumDetail = MusicAlbum.objects.get(pk=album_id)
    except MusicAlbum.DoesNotExist:
        raise Http404('Music ALbum Does Not Exist')
    return render(request,"album/detail.html",{'albumdetail':albumDetail})


def songs(request):
    try:
        allSongs = MusicSong.objects.all()
    except MusicSong.DoesNotExist:
        raise Http404('Music Songs Does Not Exist')
    return render(request,"song/index.html",{'songs':allSongs})


def searchSongs(request,musicalbum):
    try:
        allSongs = MusicSong.objects.filter(musicalbum=musicalbum)
    except MusicSong.DoesNotExist:
        raise Http404('Music Songs Does Not Exist')
    return render(request,"song/index.html",{'songs':allSongs})

def songDetail(request,song_id):
    try:
        songDetail = MusicSong.objects.get(pk=song_id)
    except MusicSong.DoesNotExist:
        raise Http404('Music Songs Does Not Exist')
    return render(request,"song/detail.html",{'songdetail':songDetail})

