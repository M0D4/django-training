from django import forms


class ArtistForm(forms.Form):
    stage_name = forms.CharField()
    social_link = forms.URLField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["stage_name"] = cleaned_data.get("stage_name").strip()
        if cleaned_data["social_link"]:
            cleaned_data["social_link"] = cleaned_data.get(
                "social_link").strip()
        return cleaned_data
