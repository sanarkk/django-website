from django.urls import path
from .views import RegisterAPI, LogoutAPI, LoginAPI, UserAPI


urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
    path("me/", UserAPI.as_view(), name="userinfo"),
]
