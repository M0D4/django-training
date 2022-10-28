from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'social_link', 'approved_albums']


admin.site.register(Artist, ArtistAdmin)
