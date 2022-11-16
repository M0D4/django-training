from rest_framework.test import APIClient
from knox.models import AuthToken
import pytest


@pytest.fixture
def api_client(db):
    def auth_client(user=None):
        if not user:
            client = APIClient()
            return client
        _, token = AuthToken.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client
    return auth_client
