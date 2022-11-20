from albums.models import Album
from .serializers import AlbumGetSerializer, AlbumPostSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import IsArtist
from django.contrib.auth.mixins import PermissionRequiredMixin


app_name = 'albums'


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumPostSerializer
    permission_classes = [permissions.AllowAny, IsArtist]
    # permission_required = "IsArtist"

    def list(self, request, format=None):
        albums = Album.objects.get_approved_albums()
        serializer = AlbumGetSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, format=None):
        serializer = AlbumPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
