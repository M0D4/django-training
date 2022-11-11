from knox import views as knox_views
from .views import LoginView
from django.urls import re_path

urlpatterns = [
    re_path(r'login/', LoginView.as_view(), name='knox_login'),
    re_path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    re_path(r'logoutall/', knox_views.LogoutAllView.as_view(),
            name='knox_logoutall'),
]
