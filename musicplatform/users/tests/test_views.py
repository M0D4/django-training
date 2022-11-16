from authentication.tests.fixtures import api_client
from rest_framework import status


class TestUserView:
    username = "mostafa"
    password = "12345"

    def test_authenticated_can_get_correct_data(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client(user)
        response = client.get("/users/1/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == self.username
        assert response.data["id"] == 1

    def test_unauthenticated_can_get_correct_data(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client()  # unauthenticated
        response = client.get("/users/1/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == self.username
        assert response.data["id"] == 1

    def test_authenticated_can_put_for_self(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)

        client = api_client(user)

        obj = {'id': '1', 'username': self.username,
               'email': 'mostafa@bld.ai', 'bio': 'software engineer'}

        response = client.put("/users/1/", obj, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == 1
        assert response.data["username"] == self.username
        assert response.data["email"] == "mostafa@bld.ai"
        assert response.data["bio"] == "software engineer"

    def test_unauthenticated_cant_put(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)

        client = api_client()

        obj = {'id': '1', 'username': self.username,
               'email': 'mostafa@bld.ai', 'bio': 'software engineer'}

        response = client.put("/users/1/", obj, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_cant_put_for_others(self, django_user_model, api_client):
        django_user_model.objects.create_user(
            username="ahmed", password=self.password)

        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)

        client = api_client(user)

        obj = {'id': '1', 'username': "ahmed",
               'email': 'ahmed@bld.ai', 'bio': 'software engineer'}

        response = client.put("/users/1/", obj, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
