from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'stage_name', 'social_link', 'user']
