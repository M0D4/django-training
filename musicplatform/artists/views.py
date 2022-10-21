from django.http import HttpResponse
from django.shortcuts import render
from artists.models import Artist

app_name = 'artists'


def create(request):
    return HttpResponse("You are adding an artist")


def index(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/index.html', context)
