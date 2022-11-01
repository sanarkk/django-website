from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_profile/user_profile.html"

    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})
