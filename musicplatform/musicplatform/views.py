from django.views import View
from .forms import SignInForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

app_name = 'music platform'


class SignInView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        form = SignInForm()
        self.context["form"] = form
        return render(request, 'musicplatform/signin.html', self.context)

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST or None)
        self.context["form"] = form
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            self.context['object'] = user
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/artists/'))
            else:
                self.context["error_message"] = "Invalid Credentials!"

        return render(request, 'musicplatform/signin.html', self.context)
