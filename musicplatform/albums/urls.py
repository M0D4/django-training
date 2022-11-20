from django.urls import path
from albums import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('albums/', views.AlbumList.as_view(), name='albums'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
