from artists.models import Artist
from artists.serializers import ArtistSerializer
from rest_framework import generics, permissions

app_name = 'artists'


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super().list(self, request, *args, **kwargs)
