from rest_framework import serializers
from albums.models import Album
from artists.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'released', 'cost']
