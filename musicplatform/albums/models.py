from artists.models import Artist
from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="New Album")
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(
        blank=False, max_digits=6, decimal_places=2, default=0)
    approved = models.BooleanField(
        default=False, help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return self.name
