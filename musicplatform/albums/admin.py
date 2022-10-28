from django.contrib import admin
from .models import Album, Song
from .forms import SongForm


class AlbumAdmin(admin.ModelAdmin):
    fields = ['artist', 'name', 'created',
              'released', 'cost', 'approved']
    readonly_fields = ['created']


admin.site.register(Album, AlbumAdmin)


class SongAdmin(admin.ModelAdmin):
    exclude = ['image_thumbnail']
    form = SongForm
    #readonly_fields = ['image_thumbnail']


admin.site.register(Song, SongAdmin)
