from django import forms
from albums.models import Song, Album


class AlbumForm(forms.ModelForm):
    approved = forms.BooleanField(required=False,
                                  help_text="Approve the album if its name is not explicit")

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["name"] = cleaned_data.get("name").strip()
        return cleaned_data

    class Meta:
        model = Album
        fields = '__all__'


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
