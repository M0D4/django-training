from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.stage_name

    def approved_albums(self):
        return self.album_set.filter(approved=True).count()

    class Meta:
        ordering = ["stage_name"]
