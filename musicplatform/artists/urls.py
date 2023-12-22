from django.urls import path
from artists import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artists'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
