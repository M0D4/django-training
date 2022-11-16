from authentication.tests.fixtures import api_client
from rest_framework import status


class TestLogin:
    username = "mostafa"
    password = "12345"

    def test_login_post_return_correct_data(self, django_user_model, api_client):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client()
        obj = {'username': self.username, 'password': self.password}
        response = client.post('/authentication/login/', obj, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data["user"]["username"] == self.username
        assert response.data["token"] is not None

    def test_login_post_must_include_username_and_password(self, api_client):
        client = api_client()
        obj = {}
        response = client.post('/authentication/login/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        error_message = response.data['username'][0]
        assert error_message == "This field is required."
        error_message = response.data['password'][0]
        assert error_message == "This field is required."


class TestRegister:
    username = "mostafa"
    email = "mostafa@bld.ai"
    password = "12345fdf4545fd##^"

    def test_register_post_return_correct_data(self, api_client):
        client = api_client()
        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password}

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == self.username
        assert response.data["email"] == self.email

    def test_register_post_password_must_pass_validation(self, api_client):
        client = api_client()
        self.password = "12345"

        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password}

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["password1"][0].code == "password_too_short"
        assert response.data["password1"][1].code == "password_too_common"

    def test_register_post_passwords_must_match(self, api_client):
        client = api_client()

        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password + "55555"}

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["password1"][0] == "Password fields don't match"

    def test_register_post_email_must_pass_validation(self, api_client):
        client = api_client()

        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password}

        response = client.post('/authentication/register/', obj, format='json')

        obj["username"] = "ahmedsaid"

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["email"][0] == "This field must be unique."

    def test_register_post_must_include_required_data(self, api_client):
        client = api_client()

        obj = {}
        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        error_message = response.data['username'][0]
        assert error_message == "This field is required."
        error_message = response.data['email'][0]
        assert error_message == "This field is required."
        error_message = response.data['password1'][0]
        assert error_message == "This field is required."
        error_message = response.data['password2'][0]
        assert error_message == "This field is required."
