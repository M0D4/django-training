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


class AlbumListManualFilter(generics.ListCreateAPIView):
    queryset = Album.objects.get_approved_albums()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsArtist]

    def list(self, request, format=None):
        gte = request.GET.get('cost__gte', 0)
        lte = request.GET.get('cost__lte', None)
        name = request.GET.get('name', '')

        if lte:
            albums = self.queryset.filter(
                cost__gte=gte, cost__lte=lte, name__icontains=name)
        else:
            albums = self.queryset.filter(
                cost__gte=gte, name__icontains=name)

        self.queryset = albums
        return super().list(self, request, format)

    def create(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
