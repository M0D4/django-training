from django.db import IntegrityError
from django.shortcuts import render
from artists.models import Artist
from .forms import ArtistForm
from django.views import View

app_name = 'artists'


class CreateView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        form = ArtistForm()
        self.context["form"] = form
        self.context["created"] = False
        return render(request, 'artists/create.html', self.context)

    def post(self, request, *args, **kwargs):
        form = ArtistForm(request.POST or None)
        self.context["form"] = form
        if form.is_valid():
            stage_name = form.cleaned_data.get("stage_name")
            social_link = form.cleaned_data.get("social_link")
            try:
                artist = Artist.objects.create(stage_name=stage_name,
                                               social_link=social_link)
                self.context['object'] = artist
                self.context['created'] = True
                self.context['form'] = ArtistForm()
            except (KeyError, IntegrityError):
                self.context["error_message"] = "Artist with same name already exist!"
                self.context["created"] = False
        return render(request, 'artists/create.html', self.context)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        artist_list = Artist.objects.all()
        context = {'artist_list': artist_list}
        return render(request, 'artists/index.html', context)
