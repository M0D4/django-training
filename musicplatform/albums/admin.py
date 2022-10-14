from django.contrib import admin
from .models import Album

# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    fields = ['artist', 'name', 'creation_datetime',
              'release_datetime', 'cost', 'approved']
    readonly_fields = ['creation_datetime']


admin.site.register(Album, AlbumAdmin)
