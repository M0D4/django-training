from django import forms
from artists.models import Artist
from albums.models import Song


class AlbumForm(forms.Form):
    # those lines will not work if I don't have a database called artist so for example if this was my first time to run this project and I have tpo makemigrations I will not be able to do this
    # because there is not artist table exists so you forgot to take this special case with you -5
    artist_list = []
    for artist in Artist.objects.all():
        artist_list.append((artist.id, artist.stage_name))

    artist = forms.CharField(widget=forms.Select(choices=artist_list))
    name = forms.CharField(required=False)
    release_datetime = forms.DateTimeField()
    cost = forms.DecimalField(required=False)
    approved = forms.BooleanField(required=False,
                                  help_text="Approve the album if its name is not explicit")

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["name"] = cleaned_data.get("name").strip()
        return cleaned_data


class SongForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["name"] = cleaned_data["name"].strip()
        if not cleaned_data["name"] or cleaned_data["name"] == "":
            cleaned_data["name"] = cleaned_data["album"].name
        return cleaned_data

    class Meta:
        model = Song
        fields = ['album', 'name', 'image', 'audio']
