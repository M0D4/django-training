from django import forms


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data["username"] = cleaned_data["username"].strip()
        return cleaned_data
