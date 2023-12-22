from django_filters import rest_framework as filters
from .models import Album


class AlbumFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = {
            'cost': ['lte', 'gte'],
        }
