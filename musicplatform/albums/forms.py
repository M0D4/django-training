from albums.models import Album
from django import forms
from artists.models import Artist


class AlbumForm(forms.Form):
    artist_list = []
    for artist in Artist.objects.all():
        artist_list.append(tuple((artist.id, artist.stage_name)))

    artist = forms.CharField(
        label="Artist: ", widget=forms.Select(choices=artist_list))
    name = forms.CharField(required=False)
    release_datetime = forms.DateTimeField()
    cost = forms.DecimalField(required=False)
    approved = forms.BooleanField(required=False,
                                  help_text="Approve the album if its name is not explicit")

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["name"] = cleaned_data.get("name").strip()
        return cleaned_data
