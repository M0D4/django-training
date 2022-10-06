from django.db import models

# Create your models here.


class Artist(models.Model):
    stage_name = models.CharField(
        max_length=200, unique=True, blank=False)
    social_link = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ["stage_name"]
