from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from core.settings.base import STATICFILES_DIRS, STATIC_URL, STATIC_ROOT
from djangoauth.models import UserProfile
# Create your views here


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_profile/user_profile.html"
    print(STATICFILES_DIRS)
    print(STATIC_ROOT)
    print(STATIC_URL)

    login_url = "/login/"
    raise_exception = True

    def get(self, request, **kwargs):
        return self.render_to_response({})


class UploadPhotoView(LoginRequiredMixin, TemplateView):
    template_name = ""