"""
Definition of urls for MusicWorld.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^genre/search/(?P<genrename>[a-z]+)$',app.views.searchGenres,name='genredetail'),
    url(r'^album/search/(?P<genrename>[a-z]+)$',app.views.searchAlbums,name='albumdetail'),
    url(r'^song/search/(?P<musicalbum>[\w\-]+)/$',app.views.searchSongs,name='songdetail'),
    url(r'^genre/detail/(?P<genre_id>[0-9]+)$',app.views.genresDetail,name='searchgenre'),
    url(r'^album/detail/(?P<album_id>[0-9]+)$',app.views.albumDetail,name='searchalbum'),
    url(r'^song/detail/(?P<song_id>[0-9]+)$',app.views.songDetail,name='searchsong'),
    url(r'^genre$',app.views.genres,name='genres'),
    url(r'^album',app.views.albums,name='albums'),
    url(r'^song',app.views.songs,name='songs')   
   

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
