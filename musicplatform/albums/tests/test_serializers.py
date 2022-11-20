from albums.models import Album
from artists.models import Artist
import pytest
from albums.serializers import AlbumSerializer
from datetime import datetime
import collections


@pytest.mark.django_db
class TestAlbumSerializer:
    username = "mostafa"
    password = "12345"

    def test_valid_deserializer(self):
        album = {
            'name': 'Hello',
            'released': '2022-10-02T09:03:59.342380Z',
            'cost': '50.00',
            'approved': True,
        }

        serializer = AlbumSerializer(data=album)
        assert serializer.is_valid()
        assert serializer.data == album
        assert serializer.errors == {}

    def test_valid_serializer(self, django_user_model):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)

        album1 = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00)

        album2 = Album.objects.create(
            artist=artist, name="The Moon", released='2022-10-15T09:03:59.342380Z', cost=100.00)

        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)

        artistDict = {
            'id': artist.id,
            'stage_name': artist.stage_name,
            'social_link': artist.social_link,
        }
        album1_serializer_data = serializer.data[0]
        assert album1_serializer_data["id"] == album1.id
        assert album1_serializer_data["name"] == album1.name
        assert float(album1_serializer_data["cost"]) == album1.cost
        assert album1_serializer_data["approved"] == album1.approved
        assert album1_serializer_data["released"] == album1.released
        assert dict(album1_serializer_data["artist"]) == artistDict
        album2_serializer_data = serializer.data[1]
        assert serializer.data[1]["id"] == album2.id
        assert album2_serializer_data["name"] == album2.name
        assert float(album2_serializer_data["cost"]) == album2.cost
        assert album2_serializer_data["approved"] == album2.approved
        assert album2_serializer_data["released"] == album2.released
        assert dict(album2_serializer_data["artist"]) == artistDict

    def test_invalid_deserializer(self):
        album = {
            'name': 'Hello',
            'cost': '50.00',
            'approved': True,
        }

        serializer = AlbumSerializer(data=album)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.errors["released"][0] == "This field is required."
