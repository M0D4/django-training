```Python

# create some artists
a = Artist(stage_name="Moustafa")
a.save()

b = Artist(stage_name="Mohamed", social_link="fb.me/mohamed")
b.save()

# list down all artists
Artist.objects.all()
# <QuerySet [<Artist: Mohamed>, <Artist: Moustafa>]>

# list down all artists sorted by name
Artist.objects.order_by("stage_name")
# <QuerySet [<Artist: Mohamed>, <Artist: Moustafa>]>

c = Artist(stage_name="Ahmed", social_link="instagram.com/ahmed")
c.save()

# list down all artists whose name starts with `a`
Artist.objects.filter(stage_name__startswith="a")
# <QuerySet [<Artist: Ahmed>]>


```
