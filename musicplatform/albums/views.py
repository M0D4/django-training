from django.db import IntegrityError
from django.shortcuts import render
from albums.models import Album
from artists.models import Artist
from .forms import AlbumForm

app_name = 'albums'


def create(request):
    form = AlbumForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        artist = Artist.objects.get(id=form.cleaned_data.get("artist"))
        name = form.cleaned_data.get("name")

        if name == "":
            name = "New Album"
        released = form.cleaned_data.get("release_datetime")
        cost = form.cleaned_data.get("cost")
        if not cost:
            cost = 0
        approved = form.cleaned_data.get("approved")
        if not approved:
            approved = False

        try:
            album = Album.objects.create(
                artist=artist, name=name, released=released, cost=cost, approved=approved)
            context['object'] = album
            context['created'] = True
        except (KeyError, IntegrityError):
            context["error_message"] = "An error occurred!"
    return render(request, 'albums/create.html', context)
