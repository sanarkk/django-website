from allauth.account.views import SignupView
from django.views.generic import TemplateView

from .forms import CustomSignupForm


# Create your views here.
class Home(TemplateView):
    template_name = "home_page.html"


class MainPage(TemplateView):
    template_name = "main_page.html"


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
