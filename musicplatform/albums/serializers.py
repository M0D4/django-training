from rest_framework import serializers
from albums.models import Album
from artists.serializers import ArtistSerializer
from artists.models import Artist


class AlbumGetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'released', 'cost']


class AlbumPostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    class Meta:
        model = Album
        fields = ['name', 'released', 'cost', 'approved']
