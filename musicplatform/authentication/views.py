from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from users.serializers import UserSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.response import Response
from users.models import User
from .serializers import RegisterSerializer


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthTokenSerializer
    queryset = User.objects.all()

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        _, token = AuthToken.objects.create(user)
        return Response({
            "token": token,
            "user": UserSerializer(user).data
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer
