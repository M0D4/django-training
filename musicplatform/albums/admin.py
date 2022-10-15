from django.contrib import admin
from .models import Album, Artist


class AlbumAdmin(admin.ModelAdmin):
    fields = ['artist', 'name', 'creation_datetime',
              'release_datetime', 'cost', 'approved']
    readonly_fields = ['creation_datetime']


admin.site.register(Album, AlbumAdmin)


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'social_link', 'approved_albums']
    inlines = [AlbumInline]


admin.site.register(Artist, ArtistAdmin)
