from albums.models import Album
from django import forms
from artists.models import Artist

# try to use meta for simplicity as you wrote a lot of code to generate the form -3
# example
#  class Meta:
#         model = Albums
#         fields = '__all__'

class AlbumForm(forms.Form):
    artist_list = []
    for artist in Artist.objects.all(): # not optimized -3
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
