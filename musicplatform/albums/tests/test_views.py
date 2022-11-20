from authentication.tests.fixtures import api_client
from rest_framework import status
from artists.models import Artist
from albums.models import Album


class TestAlbumList:
    username = "mostafa"
    password = "12345"

    def test_authenticated_can_get(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        response = client.get('/albums/')
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_can_get(self, api_client):
        client = api_client()
        response = client.get('/albums/')
        assert response.status_code == status.HTTP_200_OK

    def test_authenticated_user_artist_can_post_and_return_correct_data(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album = {
            'name': 'Hello',
            'released': '2022-10-02T09:03:59.342380Z',
            'cost': '50.00',
            'approved': True,
        }
        artistDict = {
            'id': artist.id,
            'stage_name': artist.stage_name,
            'social_link': artist.social_link,
            'user': artist.user.id
        }
        client = api_client(user)
        response = client.post('/albums/', album, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] == 1
        assert response.data["name"] == album["name"]
        assert response.data["cost"] == album["cost"]
        assert response.data["released"] == album["released"]
        assert response.data["approved"] == album["approved"]
        assert response.data["artist"] == artistDict

    def test_unauthenticated_cant_post(self, api_client):
        client = api_client()
        album = {
            'name': 'Hello',
            'released': '2022-10-02T09:03:59.342380Z',
            'cost': '50.00',
            'approved': True,
        }
        response = client.post('/albums/', album, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_user_not_artist_cant_post(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        album = {
            'name': 'Hello',
            'released': '2022-10-02T09:03:59.342380Z',
            'cost': '50.00',
            'approved': True,
        }
        response = client.post('/albums/', album, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_view_uses_the_expected_serializer(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00, approved=True)
        client = api_client()
        response = client.get('/albums/')
        albumDict = response.data["results"][0]
        artistDict = {
            'id': album.artist.id,
            'stage_name': album.artist.stage_name,
            'social_link': album.artist.social_link,
            'user': album.artist.user.id
        }
        assert response.status_code == status.HTTP_200_OK
        assert albumDict["id"] == album.id
        assert albumDict["name"] == album.name
        assert albumDict["released"] == album.released
        assert float(albumDict["cost"]) == album.cost
        assert albumDict["approved"] == album.approved
        assert albumDict["artist"] == artistDict
