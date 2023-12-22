from rest_framework import permissions, generics
from .serializers import UserSerializer
from .models import User
from .permissions import IsSameUser


class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny, IsSameUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
