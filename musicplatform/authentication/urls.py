from knox import views as knox_views
from .views import LoginView, RegisterView
from django.urls import re_path, path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    re_path(r'login/', LoginView.as_view(), name='knox_login'),
    re_path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    re_path(r'logoutall/', knox_views.LogoutAllView.as_view(),
            name='knox_logoutall'),
]
