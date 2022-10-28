from django.contrib import admin
from .models import Album, Song
from .forms import SongForm
from django import forms


class SongInline(admin.TabularInline):
    model = Song
    extra = 0
    min_num = 1


class AlbumAdmin(admin.ModelAdmin):
    fields = ['artist', 'name', 'created',
              'released', 'cost', 'approved']
    readonly_fields = ['created']
    inlines = [SongInline]


admin.site.register(Album, AlbumAdmin)


class SongAdmin(admin.ModelAdmin):
    exclude = ['image_thumbnail']
    form = SongForm
    #readonly_fields = ['image_thumbnail']

    def delete_model(self, request, obj):
        if obj.album.song_set.count() == 1:
            raise forms.ValidationError("Album Can't be empty")
        obj.delete()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Song, SongAdmin)
