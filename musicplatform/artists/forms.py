from django import forms
from artists.models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["stage_name"] = cleaned_data.get("stage_name").strip()
        if cleaned_data["social_link"]:
            cleaned_data["social_link"] = cleaned_data.get(
                "social_link").strip()
        return cleaned_data
