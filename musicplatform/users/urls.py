from .views import UserView
from django.urls import path

urlpatterns = [
    path('users/<pk>/', UserView.as_view(), name='user-view'),
]
