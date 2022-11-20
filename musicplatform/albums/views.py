from .models import Album
from .serializers import AlbumSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import IsArtist
from .filters import AlbumFilter

app_name = 'albums'


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.get_approved_albums()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsArtist]
    filterset_class = AlbumFilter

    def create(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
