from django.db import IntegrityError
from django.shortcuts import render
from artists.models import Artist
from .forms import ArtistForm

app_name = 'artists'


def create(request):
    form = ArtistForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        stage_name = form.cleaned_data.get("stage_name")
        social_link = form.cleaned_data.get("social_link")
        try:
            artist = Artist.objects.create(stage_name=stage_name,
                                           social_link=social_link)
            context['object'] = artist
            context['created'] = True
        except (KeyError, IntegrityError):
            context["error_message"] = "Artist with same name already exist!"
    return render(request, 'artists/create.html', context)


def index(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/index.html', context)
