```Python

from artists.models import Artist
from albums.models import Album
from django.utils import timezone
import datetime

# create some artists
artist1 = Artist(stage_name="Moustafa")
artist1.save()

artist2 = Artist(stage_name="Mohamed", social_link="fb.me/mohamed")
artist2.save()

# list down all artists
Artist.objects.all()
# <QuerySet [<Artist: Mohamed>, <Artist: Moustafa>]>

# list down all artists sorted by name
Artist.objects.order_by("stage_name")
# <QuerySet [<Artist: Mohamed>, <Artist: Moustafa>]>

artist3 = Artist(stage_name="Ahmed", social_link="instagram.com/ahmed")
artist3.save()

# list down all artists whose name starts with `a`
Artist.objects.filter(stage_name__startswith="a")
# <QuerySet [<Artist: Ahmed>]>

# in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)
album1 = Album(artist = artist1, name = "de7k", release_datetime = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380), cost=25.50)
album1.save()

album2 = Album(name = "Hello", release_datetime = datetime.datetime(2022, 10, 2, 9, 3, 59, 342380), cost=75.50)
album2.artist = artist2
album2.save()

artist3.album_set.create(name = "The Moon", release_datetime = datetime.datetime(2020, 8, 11, 9, 3, 59, 342380), cost=12.50)

artist3.album_set.create(name = "The Moon 2", release_datetime = datetime.datetime(2022, 10, 7, 9, 3, 59, 342380), cost=12.50)

# get the latest released album
Album.objects.order_by("-release_datetime")[0]

# get all albums released before today
current_year = timezone.now().year
current_month = timezone.now().month
current_day = timezone.now().day

Album.objects.filter(release_datetime__lt=datetime.date(current_year, current_month, current_day))
# <QuerySet [<Album: de7k>, <Album: Hello>, <Album: The Moon>]>

# get all albums released today or before but not after today
Album.objects.filter(release_datetime__lte=datetime.date(current_year, current_month, current_day))


# count the total number of albums (hint: count in an optimized manner)
Album.objects.count()
# 4

# in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)

for artist in Artist.objects.all():
    artist.album_set.all()

"""
<QuerySet [<Album: The Moon>, <Album: The Moon 2>]>
<QuerySet [<Album: Hello>]>
<QuerySet [<Album: de7k>]>
"""
for artist_ in Artist.objects.all():
    Album.objects.filter(artist=artist_)

"""
<QuerySet [<Album: The Moon>, <Album: The Moon 2>]>
<QuerySet [<Album: Hello>]>
<QuerySet [<Album: de7k>]>
"""

# list down all albums ordered by cost then by name (cost has the higher priority)
Album.objects.order_by("cost", "name")
# <QuerySet [<Album: The Moon>, <Album: The Moon 2>, <Album: de7k>, <Album: Hello>]>


```
