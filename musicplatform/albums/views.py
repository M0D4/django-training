from django.db import IntegrityError
from django.shortcuts import render
from albums.models import Album
from artists.models import Artist
from .forms import AlbumForm
from django.views import View

app_name = 'albums'


class CreateView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        form = AlbumForm()
        self.context["form"] = form
        self.context["created"] = False
        return render(request, 'albums/create.html', self.context)

    def post(self, request, *args, **kwargs):
        form = AlbumForm(request.POST or None)
        self.context["form"] = form
        if form.is_valid():
            try:
                artist = Artist.objects.get(pk=form.cleaned_data.get("artist"))
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

                album = Album.objects.create(
                    artist=artist, name=name, released=released, cost=cost, approved=approved)
                self.context['object'] = album
                form = AlbumForm()
                self.context["form"] = form
                self.context['created'] = True
            except (Artist.DoesNotExist):
                self.context["error_message"] = "This artist does not exist!"
            except (KeyError, IntegrityError):
                self.context["error_message"] = "An error occurred!"
                self.context["created"] = False
        return render(request, 'albums/create.html', self.context)
