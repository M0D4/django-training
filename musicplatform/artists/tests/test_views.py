from authentication.tests.fixtures import api_client
from rest_framework import status


class TestArtistList:
    username = "mostafa"
    password = "12345"

    def test_authenticated_can_get(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        response = client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_can_get(self, api_client):
        client = api_client()
        response = client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK

    def test_authenticated_can_post_and_return_correct_data(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        artist = {'stage_name': 'ahmed', 'social_link': '', 'user': user.id}
        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["stage_name"] == artist["stage_name"]
        assert response.data["social_link"] == artist["social_link"]
        assert response.data["user"] == artist["user"]

    def test_authenticated_post_must_include_required_field(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        artist = {'social_link': 'https://fb.xyz', 'user': user.id}
        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        error_message = response.data['stage_name'][0]
        assert error_message == "This field is required."

    def test_unauthenticated_cant_post(self, api_client):
        client = api_client()
        artist = {'stage_name': 'ahmed', 'social_link': '', 'user': None}
        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
