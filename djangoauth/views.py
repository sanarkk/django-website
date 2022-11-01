from allauth.account.views import SignupView, LoginView
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomSignupForm
from core.settings import base
from django.utils.translation import gettext_lazy as _

# Create your views here.


class MainPageView(TemplateView):
    template_name = "main_page.html"


class CustomSignupView(SuccessMessageMixin, SignupView):
    form_class = CustomSignupForm


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = _("Successfully login.")
