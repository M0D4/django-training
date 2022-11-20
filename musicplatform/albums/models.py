from artists.models import Artist
from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator


class AlbumManager(models.Manager):
    def get_approved_albums(self):
        return super().get_queryset().filter(approved=True)


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="New Album")
    released = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(
        blank=False, max_digits=6, decimal_places=2, default=0)
    approved = models.BooleanField(
        default=False, help_text="Approve the album if its name is not explicit")
    objects = AlbumManager()

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media/songsImages')
    """
    this field [image_thumbnail] maybe isn't useful because we can generate
    processed image files directly in our template without adding anything to our model
    """
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    audio = models.FileField(upload_to='media/songsAudios', validators=[
                             FileExtensionValidator(allowed_extensions=["mp3", "wav"])])

    def __str__(self):
        return self.name
