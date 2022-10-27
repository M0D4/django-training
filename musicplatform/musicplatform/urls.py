"""musicplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import artists.views
import albums.views
import musicplatform.views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-in/', musicplatform.views.SignInView.as_view(), name="sign-in"),
    path('artists/create',
         login_required(artists.views.CreateView.as_view()), name='create'),
    path('artists/', artists.views.IndexView.as_view(), name='index'),
    path('albums/create', login_required(albums.views.CreateView.as_view()), name='create')
]
