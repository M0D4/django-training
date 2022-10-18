from django.db import models
from django.db.models import Q, Count


class ArtistManager(models.Manager):
    def get_queryset(self):
        albums = Count('album', filter=Q(album__approved=True))
        return super().get_queryset().annotate(approved_albums=albums)


class Artist(models.Model):
    stage_name = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=300, null=False, blank=True)
    objects = ArtistManager()

    def __str__(self):
        return self.stage_name

    def approved_albums(self):
        return self.album_set.filter(approved=True).count()

    class Meta:
        ordering = ["stage_name"]
