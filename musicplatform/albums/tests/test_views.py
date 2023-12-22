from authentication.tests.fixtures import api_client
from rest_framework import status
from artists.models import Artist
from albums.models import Album


class TestAlbumList:
    username = "mostafa"
    password = "12345"
    base_url = '/albums/'

    def test_authenticated_can_get(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        response = client.get(self.base_url)
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_can_get(self, api_client):
        client = api_client()
        response = client.get(self.base_url)
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
        response = client.post(self.base_url, album, format='json')
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
        response = client.post(self.base_url, album, format='json')
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
        response = client.post(self.base_url, album, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_view_uses_the_expected_serializer(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00, approved=True)
        client = api_client()
        response = client.get(self.base_url)
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

    def test_get_with_filter(self, django_user_model, api_client):
        print(self.base_url)
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album1 = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00, approved=True)
        album2 = Album.objects.create(
            artist=artist, name="Hello World", released='2022-10-15T09:03:59.342380Z', cost=20.00, approved=True)
        album3 = Album.objects.create(
            artist=artist, name="The Moon", released='2022-11-10T09:03:59.342380Z', cost=150.00, approved=True)
        client = api_client()
        response = client.get(self.base_url+'?name=hello')
        assert response.data["count"] == 2  # album1 and album2
        response = client.get(self.base_url+'?cost__gte=25')
        assert response.data["count"] == 2  # album1 and album3
        response = client.get(self.base_url+'?cost__gte=25&cost__lte=80')
        assert response.data["count"] == 1  # album2
        response = client.get(
            self.base_url+'?name=e&cost__gte=10&cost__lte=250')
        assert response.data["count"] == 3  # all
        response = client.get(
            self.base_url+'?name=Hello&cost__gte=60&cost__lte=100')
        assert response.data["count"] == 0  # None


class TestAlbumListWithManualFilter:
    username = "mostafa"
    password = "12345"
    base_url = '/albums/manual-filter/'

    def test_authenticated_can_get(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        response = client.get(self.base_url)
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_can_get(self, api_client):
        client = api_client()
        response = client.get(self.base_url)
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
        response = client.post(self.base_url, album, format='json')
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
        response = client.post(self.base_url, album, format='json')
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
        response = client.post(self.base_url, album, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_view_uses_the_expected_serializer(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00, approved=True)
        client = api_client()
        response = client.get(self.base_url)
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

    def test_get_with_filter(self, django_user_model, api_client):
        print(self.base_url)
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        artist = Artist.objects.create(stage_name='mostafa', user=user)
        album1 = Album.objects.create(
            artist=artist, name="Hello", released='2022-10-02T09:03:59.342380Z', cost=50.00, approved=True)
        album2 = Album.objects.create(
            artist=artist, name="Hello World", released='2022-10-15T09:03:59.342380Z', cost=20.00, approved=True)
        album3 = Album.objects.create(
            artist=artist, name="The Moon", released='2022-11-10T09:03:59.342380Z', cost=150.00, approved=True)
        client = api_client()
        response = client.get(self.base_url+'?name=hello')
        assert response.data["count"] == 2  # album1 and album2
        response = client.get(self.base_url+'?cost__gte=25')
        assert response.data["count"] == 2  # album1 and album3
        response = client.get(self.base_url+'?cost__gte=25&cost__lte=80')
        assert response.data["count"] == 1  # album2
        response = client.get(
            self.base_url+'?name=e&cost__gte=10&cost__lte=250')
        assert response.data["count"] == 3  # all
        response = client.get(
            self.base_url+'?name=Hello&cost__gte=60&cost__lte=100')
        assert response.data["count"] == 0  # None
