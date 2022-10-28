from django.contrib import admin
from .models import Album, Song
from .forms import SongForm
from django.contrib import messages


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


class RemoveAdminDefaultMessageMixin:

    def remove_default_message(self, request):
        storage = messages.get_messages(request)
        try:
            del storage._queued_messages[-1]
        except KeyError:
            pass
        return True

    def response_delete(self, request, obj_display, obj_id):
        """override"""
        response = super().response_delete(request, obj_display, obj_id)
        self.remove_default_message(request)
        return response

    def response_queryset_delete(self, request, obj_display, query_set):
        """override"""
        response = super().response_queryset_delete(request, obj_display, query_set)
        self.remove_default_message(request)
        return response


class SongAdmin(RemoveAdminDefaultMessageMixin, admin.ModelAdmin):
    exclude = ['image_thumbnail']
    form = SongForm
    #readonly_fields = ['image_thumbnail']

    def delete_model(self, request, obj):
        if obj.album.song_set.count() == 1:
            self.message_user(
                request, 'There should be at least 1 song left in each album.', level=messages.ERROR)
        else:
            self.message_user(
                request, 'The song “{}” was deleted successfully.'.format(obj)
            )
            obj.delete()

    def delete_queryset(self, request, queryset):
        freq = {}
        for song in queryset:
            if song.album.id in freq:
                freq[song.album.id] += 1
            else:
                freq[song.album.id] = 1

        can_delete = True
        for id in freq:
            if Album.objects.get(pk=id).song_set.count() - freq[id] < 1:
                can_delete = False

        if can_delete:
            return super().delete_queryset(request, queryset)
        else:
            self.message_user(
                request, 'There should be at least 1 song left in each album.', level=messages.ERROR)


admin.site.register(Song, SongAdmin)
