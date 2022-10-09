from django.urls import path, include
from .views import RegisterAPI, LogoutAPI, LoginAPI, UserAPI, DashboardAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
    path("me/", UserAPI.as_view(), name="userinfo"),
    path("dashboard/", DashboardAPI.as_view(), name="dashboard"),
]
