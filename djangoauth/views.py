from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

from .forms import CustomSignupForm


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})


class MainPage(TemplateView):
    template_name = "main_page.html"


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
