from django.urls import path
from albums import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('albums/create', login_required(views.CreateView.as_view()), name='create')
]
