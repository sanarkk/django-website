from allauth.account.views import SignupView, LoginView
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomSignupForm
from core.settings import base
from django.utils.translation import gettext_lazy as _

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})


class MainPageView(TemplateView):
    template_name = "main_page.html"


class SwitcherView(TemplateView):
    template_name = "switcher.html"


class CustomSignupView(SuccessMessageMixin, SignupView):
    form_class = CustomSignupForm


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = _("Successfully login.")
